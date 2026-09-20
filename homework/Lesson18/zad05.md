# Zadanie 5 – Cykliczne rezerwacje

## Cel zadania

Celem zadania było dodanie do aplikacji możliwości tworzenia i obsługi cyklicznych rezerwacji sal.

System umożliwia:

- tworzenie rezerwacji powtarzających się co tydzień (`WEEKLY`),
- tworzenie rezerwacji powtarzających się co dwa tygodnie (`BIWEEKLY`),
- połączenie wszystkich rezerwacji z jednej serii za pomocą wspólnego `series_id`,
- anulowanie pojedynczej rezerwacji,
- anulowanie całej serii,
- sprawdzanie konfliktów dla wszystkich terminów przed utworzeniem serii.

Do generowania terminów cyklicznych wykorzystałam bibliotekę `python-dateutil`.

---

## 1. Rozszerzenie modelu Booking

W modelu `Booking` w pliku:

```text
app/models.py
```

dodałam dwa nowe pola:

```python
recurrence_rule = db.Column(
    db.String(20),
    nullable=True
)

series_id = db.Column(
    db.String(36),
    nullable=True,
    index=True
)
```

### recurrence_rule

Pole:

```python
recurrence_rule
```

przechowuje informację o częstotliwości rezerwacji.

Obsługiwane wartości:

```text
WEEKLY
BIWEEKLY
```

`WEEKLY` oznacza rezerwację co tydzień, natomiast `BIWEEKLY` oznacza rezerwację co dwa tygodnie.

### series_id

Pole:

```python
series_id
```

przechowuje UUID wspólny dla wszystkich rezerwacji należących do tej samej serii.

Przykład:

```text
series_id:
54af1ef0-0523-4fbc-96df-1753e42f6d33
```

Dzięki temu można rozpoznać, które rezerwacje należą do jednej serii.

---

## 2. Aktualizacja bazy danych

Do istniejącej tabeli `bookings` zostały dodane nowe kolumny:

```sql
ALTER TABLE bookings
ADD COLUMN IF NOT EXISTS recurrence_rule VARCHAR(20);
```

oraz:

```sql
ALTER TABLE bookings
ADD COLUMN IF NOT EXISTS series_id VARCHAR(36);
```

Dzięki temu struktura tabeli w PostgreSQL odpowiada aktualnemu modelowi `Booking`.

---

## 3. Obsługa cyklicznych rezerwacji

Utworzyłam nowy plik:

```text
app/routes/recurring_bookings.py
```

Znajdują się w nim endpointy odpowiedzialne za:

```text
POST /api/bookings/series
```

– utworzenie serii,

```text
POST /api/bookings/<id>/cancel
```

– anulowanie pojedynczej rezerwacji,

```text
POST /api/bookings/series/<series_id>/cancel
```

– anulowanie całej serii.

Dla nowych endpointów utworzyłam Blueprint:

```python
recurring_bookings_bp = Blueprint(
    'recurring_bookings',
    __name__
)
```

Blueprint został zarejestrowany w:

```text
app/__init__.py
```

za pomocą:

```python
from app.routes.recurring_bookings import recurring_bookings_bp

app.register_blueprint(
    recurring_bookings_bp
)
```

---

## 4. Tworzenie serii rezerwacji

Do tworzenia serii służy endpoint:

```text
POST /api/bookings/series
```

Endpoint przyjmuje dane dotyczące pierwszej rezerwacji oraz regułę cykliczności.

Przykładowe dane:

```json
{
    "room_id": 1,
    "user_id": 1,
    "title": "Cotygodniowe spotkanie",
    "description": "Test cyklicznej rezerwacji",
    "start_time": "2026-09-20T12:00:00",
    "end_time": "2026-09-20T13:00:00",
    "recurrence_rule": "WEEKLY",
    "months": 3,
    "attendees_count": 4
}
```

System sprawdza wartość `recurrence_rule`.

Dla:

```text
WEEKLY
```

ustawiany jest interwał:

```python
interval = 1
```

a dla:

```text
BIWEEKLY
```

ustawiany jest:

```python
interval = 2
```

---

## 5. Generowanie terminów – python-dateutil

Do generowania terminów wykorzystałam:

```python
from dateutil.rrule import rrule, WEEKLY
```

oraz:

```python
from dateutil.relativedelta import relativedelta
```

Koniec serii obliczany jest na podstawie liczby miesięcy:

```python
series_end = (
    start_time
    + relativedelta(months=months)
)
```

Następnie `rrule` generuje wszystkie daty:

```python
occurrence_starts = list(
    rrule(
        WEEKLY,
        interval=interval,
        dtstart=start_time,
        until=series_end
    )
)
```

Dzięki wartości `interval` ten sam mechanizm obsługuje zarówno:

```text
WEEKLY     → co 1 tydzień
BIWEEKLY   → co 2 tygodnie
```

---

## 6. Wspólny series_id

Po sprawdzeniu poprawności wszystkich terminów generowany jest UUID:

```python
series_id = str(
    uuid.uuid4()
)
```

Następnie każda rezerwacja utworzona w ramach serii otrzymuje:

```python
recurrence_rule=recurrence_rule,
series_id=series_id
```

Dzięki temu wszystkie wystąpienia można później znaleźć za pomocą wspólnego `series_id`.

Schemat:

```text
SERIA
  │
  └── series_id: 54af1ef0-...
          │
          ├── Booking #22
          ├── Booking #23
          ├── Booking #24
          ├── Booking #25
          └── ...
```

---

## 7. Walidacja konfliktów

Przed utworzeniem serii system sprawdza wszystkie wygenerowane terminy.

Utworzyłam funkcję:

```python
def has_booking_conflict(
    room_id,
    start_time,
    end_time
):
```

Konflikt jest wyszukiwany za pomocą warunków:

```python
Booking.room_id == room_id,
Booking.status != 'cancelled',
Booking.start_time < end_time,
Booking.end_time > start_time
```

Oznacza to, że system sprawdza, czy w tej samej sali istnieje aktywna rezerwacja nachodząca czasowo na nową rezerwację.

Anulowane rezerwacje:

```text
status = cancelled
```

nie są traktowane jako konflikty.

---

## 8. Sprawdzenie całej serii przed zapisem

System najpierw sprawdza wszystkie wygenerowane terminy, a dopiero później zapisuje rezerwacje.

Schemat:

```text
Wygenerowanie terminów
        ↓
Sprawdzenie terminu 1
        ↓
Sprawdzenie terminu 2
        ↓
Sprawdzenie terminu 3
        ↓
        ...
        ↓
Czy występuje konflikt?
     ↙         ↘
   NIE         TAK
    ↓           ↓
zapis całej   brak zapisu
   serii      całej serii
```

Jeżeli występuje przynajmniej jeden konflikt, endpoint zwraca:

```text
409 Conflict
```

wraz z informacją o konfliktujących terminach.

Dzięki temu nie powstaje niepełna seria, w której część rezerwacji zostałaby zapisana, a część odrzucona.

---

## 9. Anulowanie pojedynczej rezerwacji

Endpoint:

```text
POST /api/bookings/<id>/cancel
```

umożliwia anulowanie jednego wystąpienia z serii.

System wyszukuje rezerwację:

```python
booking = db.session.get(
    Booking,
    booking_id
)
```

i zmienia:

```python
booking.status = 'cancelled'
```

Następnie zmiana jest zapisywana:

```python
db.session.commit()
```

Anulowanie jednej rezerwacji nie powoduje anulowania pozostałych rezerwacji należących do tej samej serii.

---

## 10. Anulowanie całej serii

Endpoint:

```text
POST /api/bookings/series/<series_id>/cancel
```

wyszukuje wszystkie rezerwacje posiadające podany `series_id`:

```python
bookings = Booking.query.filter_by(
    series_id=series_id
).all()
```

Następnie wszystkie aktywne rezerwacje w serii otrzymują:

```python
booking.status = 'cancelled'
```

Dzięki temu całą serię można anulować jednym żądaniem.

---

# Testy działania

## Test 1 – utworzenie serii WEEKLY

Utworzyłam serię:

```text
Nazwa: Cotygodniowe spotkanie
Pierwszy termin: 20.09.2026, 12:00–13:00
Reguła: WEEKLY
Okres: 3 miesiące
Sala: room_id = 1
```

System zwrócił:

```text
message         : Seria rezerwacji została utworzona
recurrence_rule : WEEKLY
count           : 14
series_id       : 54af1ef0-0523-4fbc-96df-1753e42f6d33
```

W wyniku jednego żądania zostało utworzonych:

```text
14 rezerwacji
```

Wszystkie otrzymały wspólny:

```text
series_id = 54af1ef0-0523-4fbc-96df-1753e42f6d33
```

Test potwierdził poprawne działanie tworzenia cyklicznych rezerwacji.

---

## Test 2 – anulowanie pojedynczej rezerwacji

Z utworzonej serii anulowałam pojedynczą rezerwację:

```text
booking_id = 22
```

System poprawnie zmienił jej status na:

```text
cancelled
```

Pozostałe wystąpienia serii pozostały niezależnymi rezerwacjami.

---

## Test 3 – anulowanie całej serii

Następnie anulowałam serię:

```text
series_id:
54af1ef0-0523-4fbc-96df-1753e42f6d33
```

Ponieważ jedna z 14 rezerwacji została już anulowana wcześniej, system anulował pozostałe:

```text
13 rezerwacji
```

Test potwierdził, że możliwe jest niezależne anulowanie pojedynczego wystąpienia oraz całej serii.

---

## Test 4 – walidacja konfliktów

Do sprawdzenia walidacji utworzyłam rezerwację blokującą:

```text
27.09.2026
12:30–13:30
room_id = 1
```

Następnie próbowałam utworzyć serię zawierającą termin:

```text
27.09.2026
12:00–13:00
room_id = 1
```

Terminy nachodzą na siebie:

```text
Seria:       12:00 ───────── 13:00
Blokująca:          12:30 ───────── 13:30
```

System wykrył konflikt z:

```text
conflicting_booking_id: 36
```

dla terminu:

```text
start_time: 2026-09-27T12:00:00
end_time:   2026-09-27T13:00:00
```

i zwrócił:

```text
Nie można utworzyć serii.
Występują konflikty terminów.
```

Żądanie zostało odrzucone jako:

```text
409 Conflict
```

Seria nie została utworzona.

---

# Wynik

System cyklicznych rezerwacji został zaimplementowany i przetestowany.

Zrealizowane zostały:

- pole `recurrence_rule` w modelu `Booking`,
- pole `series_id`,
- generowanie UUID dla każdej serii,
- obsługa `WEEKLY`,
- obsługa `BIWEEKLY`,
- generowanie terminów za pomocą `python-dateutil` i `rrule`,
- endpoint tworzący serię rezerwacji,
- wspólne `series_id` dla wszystkich wystąpień,
- anulowanie pojedynczej rezerwacji,
- anulowanie całej serii,
- ignorowanie anulowanych rezerwacji podczas sprawdzania konfliktów,
- walidacja konfliktów dla wszystkich wystąpień przed zapisem,
- blokowanie całej serii w przypadku wystąpienia konfliktu.

Końcowy mechanizm działania:

```text
POST /api/bookings/series
          ↓
   dane pierwszej rezerwacji
          ↓
 WEEKLY / BIWEEKLY
          ↓
 python-dateutil / rrule
          ↓
 wygenerowanie terminów
          ↓
 sprawdzenie WSZYSTKICH konfliktów
          ↓
      ┌───┴────┐
      ↓        ↓
 brak        konflikt
konfliktu      ↓
      ↓     409 Conflict
series_id      ↓
      ↓     brak zapisu
utworzenie
całej serii
      ↓
 ┌────┴───────────────┐
 ↓                    ↓
anulowanie        anulowanie
jednej            całej serii
rezerwacji
```

Testy potwierdziły poprawne działanie tworzenia serii, wspólnego `series_id`, anulowania pojedynczych rezerwacji, anulowania całej serii oraz walidacji konfliktów.

