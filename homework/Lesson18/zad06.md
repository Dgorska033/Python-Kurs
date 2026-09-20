# Zadanie 6 – Eksport raportu do PDF

## Cel zadania

Celem zadania było stworzenie endpointu generującego miesięczny raport rezerwacji w formacie PDF.

Endpoint:

```text
GET /api/reports/monthly?month=YYYY-MM
```

Przykład:

```text
/api/reports/monthly?month=2026-09
```

Raport zawiera:

- podsumowanie miesiąca,
- liczbę rezerwacji,
- łączny czas rezerwacji,
- łączny przychód,
- tabelę Top 10 sal,
- tabelę Top 10 użytkowników,
- wykres wykorzystania sal.

Do generowania dokumentu PDF wykorzystałam bibliotekę:

```text
ReportLab
```

Do generowania wykresu wykorzystałam:

```text
Matplotlib
```

---

## 1. Instalacja bibliotek

Do projektu zostały dodane biblioteki:

```text
reportlab
matplotlib
```

ReportLab odpowiada za utworzenie dokumentu PDF.

Matplotlib odpowiada za wygenerowanie wykresu, który następnie jest umieszczany w raporcie jako obraz.

---

## 2. Utworzenie endpointu raportów

Utworzyłam nowy plik:

```text
app/routes/reports.py
```

oraz Blueprint:

```python
reports_bp = Blueprint(
    "reports",
    __name__
)
```

Endpoint raportu:

```python
@reports_bp.route(
    "/api/reports/monthly",
    methods=["GET"]
)
def monthly_report():
```

Raport jest więc dostępny pod adresem:

```text
GET /api/reports/monthly
```

Wybrany miesiąc przekazywany jest jako parametr:

```text
?month=YYYY-MM
```

Przykład:

```text
/api/reports/monthly?month=2026-09
```

---

## 3. Rejestracja Blueprint

Blueprint raportów został zarejestrowany w:

```text
app/__init__.py
```

za pomocą:

```python
from app.routes.reports import reports_bp

app.register_blueprint(
    reports_bp
)
```

Dzięki temu endpoint raportów jest dostępny w aplikacji Flask.

---

## 4. Pobieranie miesiąca

Endpoint pobiera parametr:

```python
month_param = request.args.get("month")
```

Oczekiwany format:

```text
YYYY-MM
```

Na przykład:

```text
2026-09
```

Następnie wartość jest zamieniana na datę:

```python
month_start = datetime.strptime(
    month_param,
    "%Y-%m"
)
```

System oblicza również początek kolejnego miesiąca.

Dzięki temu możliwe jest pobranie wszystkich rezerwacji znajdujących się pomiędzy:

```text
początkiem wybranego miesiąca
```

a:

```text
początkiem kolejnego miesiąca
```

---

## 5. Pobieranie rezerwacji

Rezerwacje pobierane są z modelu:

```text
Booking
```

za pomocą:

```python
bookings = Booking.query.filter(
    Booking.start_time >= month_start,
    Booking.start_time < next_month,
    Booking.status != "cancelled"
).all()
```

Do raportu trafiają więc tylko rezerwacje:

- rozpoczynające się w wybranym miesiącu,
- które nie zostały anulowane.

Rezerwacje posiadające:

```text
status = cancelled
```

nie są uwzględniane w statystykach.

---

## 6. Podsumowanie miesiąca

Na podstawie pobranych rezerwacji obliczane są trzy główne wartości.

### Liczba rezerwacji

```python
total_bookings = len(bookings)
```

### Łączny czas

```python
total_hours = sum(
    booking.duration_hours
    for booking in bookings
)
```

### Łączny przychód

```python
total_revenue = sum(
    booking.total_cost
    for booking in bookings
)
```

W raporcie wartości przedstawiane są w tabeli:

```text
Liczba rezerwacji
Łączny czas
Łączny przychód
```

---

## 7. Top 10 sal

Dla każdej sali obliczana jest:

- liczba rezerwacji,
- łączna liczba zarezerwowanych godzin.

Statystyki przechowywane są w:

```python
room_stats
```

Następnie sale są sortowane według liczby rezerwacji:

```python
top_rooms = sorted(
    room_stats.items(),
    key=lambda item: item[1]["bookings"],
    reverse=True
)[:10]
```

Do raportu trafia maksymalnie:

```text
10 najczęściej rezerwowanych sal
```

Tabela zawiera kolumny:

```text
Sala
Rezerwacje
Godziny
```

---

## 8. Top 10 użytkowników

Analogicznie tworzone są statystyki użytkowników.

Dla każdego użytkownika obliczana jest:

- liczba wykonanych rezerwacji,
- łączna liczba zarezerwowanych godzin.

Statystyki są następnie sortowane:

```python
top_users = sorted(
    user_stats.items(),
    key=lambda item: item[1]["bookings"],
    reverse=True
)[:10]
```

Do raportu trafia maksymalnie:

```text
10 najaktywniejszych użytkowników
```

Tabela zawiera:

```text
Użytkownik
Rezerwacje
Godziny
```

---

## 9. Wykres wykorzystania sal

Do wygenerowania wykresu wykorzystałam:

```text
Matplotlib
```

Wykres przedstawia liczbę godzin wykorzystania poszczególnych sal.

Dane wykresu tworzone są na podstawie:

```python
room_names
```

oraz:

```python
room_hours
```

Wykres tworzony jest za pomocą:

```python
plt.bar(
    room_names,
    room_hours
)
```

Oś X przedstawia:

```text
sale
```

natomiast oś Y:

```text
liczbę godzin
```

Wykres jest zapisywany jako obraz PNG do pamięci:

```python
chart_buffer = BytesIO()
```

oraz:

```python
plt.savefig(
    chart_buffer,
    format="png",
    dpi=150
)
```

Nie jest więc konieczne zapisywanie osobnego pliku wykresu na dysku.

---

## 10. Generowanie dokumentu PDF

Raport generowany jest za pomocą biblioteki:

```text
ReportLab
```

Dokument tworzony jest jako:

```python
doc = SimpleDocTemplate(
    pdf_buffer,
    pagesize=A4
)
```

Do dokumentu kolejno dodawane są:

```text
Tytuł raportu
        ↓
Podsumowanie
        ↓
Top 10 sal
        ↓
Top 10 użytkowników
        ↓
Wykres wykorzystania sal
```

Do tworzenia elementów dokumentu wykorzystałam między innymi:

```python
Paragraph
Table
TableStyle
Spacer
Image
```

Na końcu dokument jest budowany:

```python
doc.build(
    elements
)
```

---

## 11. Obsługa polskich znaków

Do poprawnego wyświetlania polskich znaków w PDF wykorzystałam font:

```text
DejaVu Sans
```

Zarejestrowane zostały dwie wersje:

```text
DejaVuSans
DejaVuSans-Bold
```

za pomocą:

```python
pdfmetrics.registerFont(
    TTFont(
        "DejaVuSans",
        "C:/Windows/Fonts/DejaVuSans.ttf"
    )
)

pdfmetrics.registerFont(
    TTFont(
        "DejaVuSans-Bold",
        "C:/Windows/Fonts/DejaVuSans-Bold.ttf"
    )
)
```

Font został zastosowany do:

- tytułów,
- nagłówków,
- zwykłego tekstu,
- tabel,
- danych znajdujących się w tabelach.

Dzięki temu raport poprawnie wyświetla między innymi:

```text
Łączny czas
Łączny przychód
Użytkownik
Wiśniewski
Dąbrowska
```

---

## 12. Zwracanie gotowego pliku

Po wygenerowaniu raport jest zwracany przez Flask jako plik PDF:

```python
return send_file(
    pdf_buffer,
    mimetype="application/pdf",
    as_attachment=True,
    download_name=(
        f"raport_{month_param}.pdf"
    )
)
```

Nazwa pliku jest automatycznie tworzona na podstawie wybranego miesiąca.

Dla:

```text
month=2026-09
```

powstaje:

```text
raport_2026-09.pdf
```

---

# Test działania

Endpoint został przetestowany dla:

```text
GET /api/reports/monthly?month=2026-09
```

Raport został poprawnie wygenerowany jako:

```text
raport_2026-09.pdf
```

Dla września 2026 raport zawierał podsumowanie:

```text
Liczba rezerwacji: 22
Łączny czas: 42.00 h
Łączny przychód: 3160.00 zł
```

Tabela najczęściej wykorzystywanych sal zawierała między innymi:

```text
Pokój Kreatywny       8 rezerwacji    16.00 h
Sala A1               7 rezerwacji    10.00 h
Sala B2               4 rezerwacje    10.00 h
Sala Konferencyjna    3 rezerwacje     6.00 h
```

Tabela użytkowników zawierała:

```text
Anna Nowak          8 rezerwacji    16.00 h
Jan Kowalski        7 rezerwacji    10.00 h
Piotr Wiśniewski    6 rezerwacji    13.00 h
Maria Dąbrowska     1 rezerwacja     3.00 h
```

W raporcie został również poprawnie wygenerowany wykres wykorzystania sal.

---

# Wynik

System generowania miesięcznych raportów PDF został zaimplementowany i przetestowany.

Zrealizowane zostały:

- endpoint `GET /api/reports/monthly`,
- wybór miesiąca przez parametr `month`,
- filtrowanie rezerwacji według miesiąca,
- pomijanie anulowanych rezerwacji,
- obliczanie liczby rezerwacji,
- obliczanie łącznego czasu,
- obliczanie łącznego przychodu,
- tabela Top 10 sal,
- tabela Top 10 użytkowników,
- wykres wykorzystania sal,
- generowanie wykresu jako obrazu,
- umieszczenie wykresu w PDF,
- generowanie dokumentu za pomocą ReportLab,
- obsługa polskich znaków,
- automatyczne zwracanie gotowego pliku PDF.

Końcowy mechanizm działania:

```text
GET /api/reports/monthly?month=2026-09
                    ↓
          odczyt parametru month
                    ↓
       ustalenie zakresu miesiąca
                    ↓
        pobranie rezerwacji z DB
                    ↓
       pominięcie anulowanych
                    ↓
        obliczenie statystyk
                    ↓
        ┌───────────┼───────────┐
        ↓           ↓           ↓
   Podsumowanie  Top 10 sal  Top 10 użytkowników
        │           │           │
        └───────────┼───────────┘
                    ↓
       wygenerowanie wykresu
                    ↓
          wygenerowanie PDF
                    ↓
          raport_2026-09.pdf
```