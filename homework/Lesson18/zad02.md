# Zadanie 2 – Analiza problemu N+1 

## Treść zadania

Dodaj do aplikacji endpoint `/debug/n-plus-1`, który:

1. Pobiera wszystkie rezerwacje bez optymalizacji.
2. Dla każdej rezerwacji wyświetla:
   - tytuł,
   - nazwę sali,
   - imię użytkownika.
3. Mierzy czas wykonania oraz liczbę wykonanych zapytań SQL.
4. Powtarza ten sam test z wykorzystaniem optymalizacji `joinedload()`.
5. Zwraca porównanie wyników w formacie JSON.

Do liczenia zapytań wykorzystany został mechanizm zdarzeń SQLAlchemy.

---

# 1. Problem N+1

Problem N+1 występuje wtedy, gdy aplikacja najpierw wykonuje jedno zapytanie pobierające główne rekordy, a następnie wykonuje kolejne zapytania podczas pobierania powiązanych danych.

W tym zadaniu głównym modelem jest:

```python
Booking
```

Każda rezerwacja posiada relacje z:

```python
Room
User
```

czyli możemy korzystać między innymi z:

```python
booking.room
booking.user
```

Jeżeli pobiorę rezerwacje w zwykły sposób:

```python
bookings = Booking.query.all()
```

SQLAlchemy pobiera rezerwacje, ale powiązane obiekty `Room` i `User` nie muszą zostać pobrane w tym samym zapytaniu.

Następnie podczas wykonywania:

```python
booking.room.name
```

oraz:

```python
booking.user.name
```

SQLAlchemy może wykonywać kolejne zapytania do bazy danych.

Schematycznie wygląda to następująco:

```text
SELECT bookings
       |
       +---- SELECT room
       |
       +---- SELECT user
       |
       +---- SELECT room
       |
       +---- SELECT user
       |
       +---- ...
```

Przy większej liczbie rekordów może to prowadzić do dużej liczby zapytań SQL i pogorszenia wydajności aplikacji.

---

# 2. Utworzenie endpointu debugowego

Do analizy problemu utworzyłam plik:

```text
app/routes/debug.py
```

W nim znajduje się Blueprint:

```python
debug_bp = Blueprint("debug", __name__)
```

oraz endpoint:

```python
@debug_bp.route("/debug/n-plus-1")
def debug_n_plus_1():
```

Endpoint jest przeznaczony do porównania działania aplikacji:

```text
bez optymalizacji
        VS
z joinedload()
```

---

# 3. Liczenie zapytań SQL

Do policzenia liczby zapytań wykorzystałam mechanizm zdarzeń SQLAlchemy.

Utworzyłam licznik:

```python
query_counter = {
    "count": 0
}
```

oraz funkcję:

```python
def count_query(
    conn,
    cursor,
    statement,
    parameters,
    context,
    executemany
):
    query_counter["count"] += 1
```

Funkcja zwiększa licznik za każdym razem, kiedy SQLAlchemy wykonuje zapytanie SQL.

Listener został podpięty do silnika SQLAlchemy:

```python
engine = db.engine

event.listen(
    engine,
    "before_cursor_execute",
    count_query
)
```

Zdarzenie:

```text
before_cursor_execute
```

jest wykonywane bezpośrednio przed wysłaniem zapytania SQL do bazy danych.

Dzięki temu mogłam policzyć rzeczywistą liczbę zapytań wykonanych podczas każdego testu.

---

# 4. Pomiar czasu

Do pomiaru czasu wykorzystałam:

```python
from time import perf_counter
```

Przed rozpoczęciem operacji zapisuję czas:

```python
start = perf_counter()
```

Po zakończeniu:

```python
end = perf_counter()
```

Czas wykonania obliczam jako:

```python
execution_time = end - start
```

Ponieważ `perf_counter()` zwraca czas w sekundach, wynik został przeliczony na milisekundy:

```python
execution_time * 1000
```

---

# 5. Test bez optymalizacji

Pierwszy test pobiera rezerwacje standardowym zapytaniem:

```python
bookings = Booking.query.all()
```

Następnie dla każdej rezerwacji pobierane są:

```python
booking.title
booking.room.name
booking.user.name
```

Dane są zapisywane do listy:

```python
without_optimization_data = []

for booking in bookings:
    without_optimization_data.append({
        "title": booking.title,
        "room": booking.room.name,
        "user": booking.user.name
    })
```

Problem polega na tym, że dostęp do:

```python
booking.room
```

oraz:

```python
booking.user
```

może powodować wykonywanie dodatkowych zapytań SQL.

Jest to przykład mechanizmu lazy loading i może prowadzić do problemu N+1.

---

# 6. Wyczyszczenie sesji przed drugim testem

Po wykonaniu pierwszego testu usuwam aktualną sesję:

```python
db.session.remove()
```

Jest to istotne, ponieważ SQLAlchemy przechowuje pobrane wcześniej obiekty w swojej sesji.

Gdybym wykonała drugi test bez wyczyszczenia sesji, część obiektów mogłaby znajdować się już w pamięci.

Mogłoby to zafałszować porównanie liczby zapytań.

---

# 7. Optymalizacja za pomocą `joinedload()`

W drugim teście wykorzystałam:

```python
joinedload()
```

Import:

```python
from sqlalchemy.orm import joinedload
```

Zapytanie wygląda następująco:

```python
bookings_optimized = Booking.query.options(
    joinedload(Booking.room),
    joinedload(Booking.user)
).all()
```

W tym przypadku SQLAlchemy wie wcześniej, że razem z rezerwacjami będą potrzebne również dane:

```text
Room
User
```

Dzięki temu może pobrać potrzebne relacje razem z głównym zapytaniem zamiast wykonywać wiele dodatkowych zapytań podczas późniejszego dostępu do relacji.

Następnie dane są odczytywane dokładnie tak samo:

```python
with_optimization_data = []

for booking in bookings_optimized:
    with_optimization_data.append({
        "title": booking.title,
        "room": booking.room.name,
        "user": booking.user.name
    })
```

Różnica polega więc nie na sposobie korzystania z obiektów, ale na sposobie ich wcześniejszego pobrania z bazy.

---

# 8. Usunięcie listenera

Listener służący do liczenia zapytań jest potrzebny tylko podczas wykonywania endpointu diagnostycznego.

Dlatego po zakończeniu testu jest usuwany:

```python
event.remove(
    engine,
    "before_cursor_execute",
    count_query
)
```

Kod znajduje się w bloku:

```python
finally:
```

Dzięki temu listener zostanie usunięty również wtedy, gdy podczas wykonywania testu wystąpi wyjątek.

Jest to ważne, ponieważ pozostawienie listenera mogłoby powodować nieprawidłowe liczenie zapytań podczas kolejnych wywołań endpointu.

---

# 9. Zwracanie wyniku jako JSON

Endpoint zwraca trzy główne części:

```text
without_optimization
with_joinedload
comparison
```

Pierwsza zawiera wynik bez optymalizacji:

```json
{
    "without_optimization": {
        "query_count": 13,
        "execution_time_ms": 32.394,
        "bookings": []
    }
}
```

Druga zawiera wynik z `joinedload()`:

```json
{
    "with_joinedload": {
        "query_count": 2,
        "execution_time_ms": 20.551,
        "bookings": []
    }
}
```

Natomiast część:

```json
{
    "comparison": {
        "booking_count": 19,
        "queries_saved": 11
    }
}
```

pokazuje bezpośrednie porównanie obu sposobów pobierania danych.

---

# 10. Rejestracja Blueprintu

Blueprint z endpointem debugowym został zarejestrowany w aplikacji.

W `app/__init__.py`:

```python
from app.routes.debug import debug_bp

app.register_blueprint(debug_bp)
```

Dzięki temu endpoint jest dostępny pod adresem:

```text
/debug/n-plus-1
```

---

# 11. Uruchomienie testu

Aplikację uruchomiłam poleceniem:

```powershell
python run.py
```

Następnie otworzyłam endpoint:

```text
http://127.0.0.1:5000/debug/n-plus-1
```

Endpoint poprawnie zwrócił dane w formacie JSON.

---

# 12. Otrzymane wyniki

Podczas testu w bazie znajdowało się:

```text
19 rezerwacji
```

### Bez optymalizacji

Otrzymałam:

```text
Liczba zapytań: 13
Czas wykonania: 32.394 ms
```

### Z `joinedload()`

Otrzymałam:

```text
Liczba zapytań: 2
Czas wykonania: 20.551 ms
```

### Porównanie

```text
Bez optymalizacji: 13 zapytań
Z joinedload():     2 zapytania

Oszczędzone zapytania: 11
```

Liczba zapytań została więc zmniejszona z:

```text
13
```

do:

```text
2
```

czyli o:

```text
11 zapytań
```

Procentowa redukcja liczby zapytań wynosi około:

```text
84,6%
```

Obliczenie:

```text
(13 - 2) / 13 * 100% ≈ 84,6%
```

---

# 13. Dlaczego przy 19 rezerwacjach nie wykonano 39 zapytań?

Teoretycznie problem N+1 mógłby wyglądać następująco:

```text
1 zapytanie o rezerwacje
+
19 zapytań o sale
+
19 zapytań o użytkowników
=
39 zapytań
```

W praktyce otrzymałam jednak:

```text
13 zapytań
```

SQLAlchemy posiada mechanizm `Identity Map`.

Jeżeli kilka rezerwacji korzysta z tego samego użytkownika lub tej samej sali, obiekt może znajdować się już w aktualnej sesji SQLAlchemy.

W takiej sytuacji ORM nie musi za każdym razem ponownie pobierać tego samego obiektu z bazy.

Dlatego rzeczywista liczba zapytań zależy między innymi od:

- liczby rezerwacji,
- liczby różnych sal,
- liczby różnych użytkowników,
- sposobu skonfigurowania relacji,
- stanu sesji SQLAlchemy.

---

# 14. Interpretacja pomiaru czasu

W moim teście czas bez optymalizacji wyniósł:

```text
32.394 ms
```

natomiast z `joinedload()`:

```text
20.551 ms
```

W tym konkretnym uruchomieniu wersja z `joinedload()` była szybsza.

Nie oznacza to jednak, że każde kolejne wykonanie będzie miało dokładnie taki sam czas.

Pomiar czasu może zależeć między innymi od:

- aktualnego obciążenia komputera,
- cache,
- stanu połączenia z bazą,
- liczby rekordów,
- innych procesów działających w systemie.

Dlatego w tym zadaniu bardziej miarodajnym wynikiem jest liczba wykonanych zapytań SQL.

Tutaj różnica jest wyraźna:

```text
13 → 2
```

---

# 15. Wniosek

Problem N+1 może wystąpić, gdy pobieramy listę obiektów, a następnie dla każdego z nich korzystamy z relacji ładowanych dopiero w momencie dostępu.

W tym przypadku zwykłe pobranie:

```python
Booking.query.all()
```

oraz późniejsze korzystanie z:

```python
booking.room
booking.user
```

spowodowało wykonanie:

```text
13 zapytań SQL
```

Zastosowanie:

```python
joinedload(Booking.room)
joinedload(Booking.user)
```

zmniejszyło liczbę zapytań do:

```text
2
```

W wyniku optymalizacji udało się uniknąć:

```text
11 zapytań
```

czyli zmniejszyć ich liczbę o około:

```text
84,6%
```

Endpoint:

```text
/debug/n-plus-1
```

poprawnie:

1. pobiera wszystkie rezerwacje,
2. odczytuje tytuł rezerwacji,
3. odczytuje nazwę sali,
4. odczytuje imię użytkownika,
5. mierzy czas wykonania,
6. liczy zapytania SQL,
7. wykonuje test bez optymalizacji,
8. wykonuje test z `joinedload()`,
9. zwraca porównanie w formacie JSON.

