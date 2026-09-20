# Zadanie 3 – Rozszerzone statystyki 

## Treść zadania

Rozszerz dashboard o:

1. **Wykres kołowy** – rozkład rezerwacji per departament.
2. **Heatmapę** – pokazującą, które godziny są najpopularniejsze w zależności od dnia tygodnia.
3. **Trend** – liczbę rezerwacji dziennie w ostatnich 30 dniach.

### Podpowiedź

Do pobierania dnia tygodnia i godziny z daty rezerwacji można wykorzystać:

```python
func.extract('dow', Booking.start_time)
```

oraz:

```python
func.extract('hour', Booking.start_time)
```

---

# 1. Rozszerzenie dashboardu

Rozszerzyłam istniejący endpoint:

```text
/dashboard
```

znajdujący się w pliku:

```text
app/routes/dashboard.py
```

Dashboard oprócz wcześniejszych statystyk wyświetla teraz trzy dodatkowe rodzaje danych:

- liczbę rezerwacji według departamentu,
- popularność godzin rezerwacji,
- trend rezerwacji z ostatnich 30 dni.

Dane są pobierane z PostgreSQL za pomocą SQLAlchemy, a następnie przekazywane do szablonu `dashboard.html`.

---

# 2. Wykres kołowy – rezerwacje według departamentu

Pierwszym elementem zadania było policzenie liczby rezerwacji wykonanych przez użytkowników z poszczególnych departamentów.

Do tego wykorzystałam tabele:

- `User`,
- `Booking`.

Zapytanie:

```python
department_stats = db.session.query(
    User.department,
    func.count(
        Booking.id
    ).label(
        'booking_count'
    )
).join(
    Booking,
    Booking.user_id == User.id
).filter(
    Booking.status != 'cancelled'
).group_by(
    User.department
).order_by(
    desc('booking_count')
).all()
```

### Jak działa zapytanie?

Najpierw pobierany jest departament użytkownika:

```python
User.department
```

Następnie:

```python
func.count(Booking.id)
```

liczy liczbę rezerwacji przypadających na dany departament.

Tabele `User` i `Booking` są połączone poprzez:

```python
Booking.user_id == User.id
```

Rezerwacje anulowane są pomijane:

```python
Booking.status != 'cancelled'
```

Na końcu wyniki są grupowane według departamentu:

```python
.group_by(User.department)
```

---

# 3. Przygotowanie danych dla wykresu kołowego

Wynik zapytania SQLAlchemy został zamieniony na listę słowników:

```python
department_data = [
    {
        'department': department or 'Brak departamentu',
        'count': booking_count
    }
    for department, booking_count
    in department_stats
]
```

Przykładowa struktura danych:

```python
[
    {
        "department": "HR",
        "count": 8
    },
    {
        "department": "Marketing",
        "count": 6
    },
    {
        "department": "IT",
        "count": 5
    }
]
```

Jeżeli użytkownik nie ma przypisanego departamentu, zostanie wyświetlona wartość:

```text
Brak departamentu
```

---

# 4. Wyświetlenie wykresu kołowego

Dane zostały przekazane z Flaska do szablonu:

```python
return render_template(
    'dashboard.html',
    stats=stats,
    upcoming=upcoming,
    top_users=top_users,
    room_utilization=room_utilization,
    department_data=department_data,
    heatmap_data=heatmap_data,
    trend_data=trend_data
)
```

Następnie dane są przekazywane z Jinja do JavaScript:

```html
<script>

    const departmentData =
        {{ department_data | tojson | safe }};

</script>
```

Filtr:

```text
tojson
```

zamienia dane Pythona na format JSON możliwy do wykorzystania w JavaScript.

---

# 5. Przygotowanie danych dla Chart.js

Z danych pobierane są osobno nazwy departamentów:

```javascript
const departmentLabels =
    departmentData.map(
        item => item.department
    );
```

oraz liczby rezerwacji:

```javascript
const departmentCounts =
    departmentData.map(
        item => item.count
    );
```

Następnie tworzony jest wykres kołowy za pomocą biblioteki Chart.js:

```javascript
new Chart(
    departmentContext,
    {
        type: "pie",

        data: {
            labels: departmentLabels,

            datasets: [
                {
                    label: "Liczba rezerwacji",
                    data: departmentCounts
                }
            ]
        }
    }
);
```

Na dashboardzie widoczny jest dzięki temu podział rezerwacji pomiędzy poszczególne departamenty.

---

# 6. Heatmapa – dzień tygodnia × godzina

Drugim wymaganiem było sprawdzenie, w jakich dniach tygodnia i o jakich godzinach rozpoczyna się najwięcej rezerwacji.

Do pobrania dnia tygodnia wykorzystałam:

```python
func.extract(
    'dow',
    Booking.start_time
)
```

Natomiast do pobrania godziny:

```python
func.extract(
    'hour',
    Booking.start_time
)
```

Całe zapytanie:

```python
heatmap_stats = db.session.query(

    func.extract(
        'dow',
        Booking.start_time
    ).label(
        'weekday'
    ),

    func.extract(
        'hour',
        Booking.start_time
    ).label(
        'hour'
    ),

    func.count(
        Booking.id
    ).label(
        'booking_count'
    )

).filter(
    Booking.status != 'cancelled'
).group_by(
    'weekday',
    'hour'
).order_by(
    'weekday',
    'hour'
).all()
```

---

# 7. `extract('dow')`

PostgreSQL zwraca dzień tygodnia jako liczbę.

W tym przypadku:

```text
0 = niedziela
1 = poniedziałek
2 = wtorek
3 = środa
4 = czwartek
5 = piątek
6 = sobota
```

Dlatego utworzyłam listę:

```python
weekdays = [
    'Nd',
    'Pn',
    'Wt',
    'Śr',
    'Cz',
    'Pt',
    'Sb'
]
```

Dzięki temu numer dnia tygodnia można zamienić na czytelną nazwę.

---

# 8. Przygotowanie danych heatmapy

Dane z bazy zostały zamienione na listę słowników:

```python
heatmap_data = [
    {
        'weekday_number': int(row.weekday),
        'weekday': weekdays[
            int(row.weekday)
        ],
        'hour': int(row.hour),
        'count': row.booking_count
    }
    for row in heatmap_stats
]
```

Każdy element zawiera:

- numer dnia tygodnia,
- nazwę dnia,
- godzinę,
- liczbę rezerwacji.

Przykładowy element:

```python
{
    "weekday_number": 1,
    "weekday": "Pn",
    "hour": 9,
    "count": 3
}
```

Oznacza to, że w poniedziałek o godzinie 9:00 rozpoczęły się 3 rezerwacje.

---

# 9. Budowanie heatmapy w JavaScript

Dane są przekazywane do JavaScript:

```javascript
const heatmapData =
    {{ heatmap_data | tojson | safe }};
```

Następnie tworzony jest słownik ułatwiający znalezienie liczby rezerwacji dla konkretnego dnia i godziny:

```javascript
const heatmapLookup = {};

heatmapData.forEach(
    item => {

        const key =
            item.weekday_number
            + "-"
            + item.hour;

        heatmapLookup[key] =
            item.count;
    }
);
```

Przykładowo klucz:

```text
1-9
```

oznacza:

```text
poniedziałek, godzina 9:00
```

---

# 10. Intensywność heatmapy

Heatmapa wykorzystuje intensywność koloru do pokazania popularności danej godziny.

Najpierw znajdowana jest największa liczba rezerwacji:

```javascript
let maxHeatmapCount = 0;

heatmapData.forEach(
    item => {

        if (
            item.count > maxHeatmapCount
        ) {
            maxHeatmapCount =
                item.count;
        }

    }
);
```

Następnie dla każdej komórki obliczana jest intensywność:

```javascript
const intensity =
    maxHeatmapCount > 0

        ? (
            0.20
            +
            (
                count
                / maxHeatmapCount
            )
            * 0.80
        )

        : 0.20;
```

Dzięki temu:

- `0` rezerwacji – jasne pole,
- mała liczba rezerwacji – jaśniejsze czerwone pole,
- większa liczba rezerwacji – ciemniejsze czerwone pole.

Pozwala to szybko zauważyć najpopularniejsze godziny.

---

# 11. Trend – ostatnie 30 dni

Trzecim elementem zadania było pokazanie liczby rezerwacji dla każdego dnia z ostatnich 30 dni.

Najpierw obliczana jest data początkowa:

```python
thirty_days_ago = (
    datetime.now().date()
    - timedelta(days=29)
)
```

Następnie wykonywane jest zapytanie:

```python
trend_stats = db.session.query(

    func.date(
        Booking.start_time
    ).label(
        'booking_date'
    ),

    func.count(
        Booking.id
    ).label(
        'booking_count'
    )

).filter(
    func.date(
        Booking.start_time
    ) >= thirty_days_ago,

    Booking.status != 'cancelled'
).group_by(
    func.date(
        Booking.start_time
    )
).order_by(
    func.date(
        Booking.start_time
    )
).all()
```

Zapytanie:

1. pobiera datę rozpoczęcia rezerwacji,
2. liczy rezerwacje dla każdego dnia,
3. pomija rezerwacje anulowane,
4. ogranicza wyniki do ostatnich 30 dni,
5. grupuje wyniki według daty.

---

# 12. Uwzględnienie dni bez rezerwacji

Samo zapytanie SQL zwróciłoby tylko dni, w których istnieje przynajmniej jedna rezerwacja.

Na wykresie chciałam jednak wyświetlić pełne 30 dni.

Dlatego najpierw tworzony jest słownik:

```python
trend_lookup = {
    row.booking_date: row.booking_count
    for row in trend_stats
}
```

Następnie generowane są wszystkie dni z badanego okresu:

```python
trend_data = []

for day_offset in range(30):

    current_date = (
        thirty_days_ago
        + timedelta(
            days=day_offset
        )
    )

    trend_data.append({
        'date': current_date.strftime(
            '%Y-%m-%d'
        ),
        'count': trend_lookup.get(
            current_date,
            0
        )
    })
```

Jeżeli dla konkretnego dnia nie znaleziono żadnej rezerwacji:

```python
trend_lookup.get(
    current_date,
    0
)
```

zwraca:

```text
0
```

Dzięki temu wykres ma ciągłą oś czasu obejmującą pełne 30 dni.

---

# 13. Wykres trendu

Dane są przekazywane do JavaScript:

```javascript
const trendData =
    {{ trend_data | tojson | safe }};
```

Następnie rozdzielane są na daty:

```javascript
const trendLabels =
    trendData.map(
        item => item.date
    );
```

oraz liczby rezerwacji:

```javascript
const trendCounts =
    trendData.map(
        item => item.count
    );
```

Wykres tworzony jest za pomocą Chart.js:

```javascript
new Chart(
    trendContext,
    {
        type: "line",

        data: {
            labels: trendLabels,

            datasets: [
                {
                    label: "Liczba rezerwacji",
                    data: trendCounts,
                    borderWidth: 2,
                    tension: 0.25,
                    fill: false
                }
            ]
        }
    }
);
```

---

# 14. Pliki zmodyfikowane w zadaniu

W ramach zadania zmodyfikowałam:

```text
app/routes/dashboard.py
```

W tym pliku dodałam zapytania odpowiedzialne za:

- statystyki według departamentu,
- dane heatmapy,
- trend ostatnich 30 dni.

Zmodyfikowałam również:

```text
app/templates/dashboard.html
```

gdzie dodałam:

- wykres kołowy,
- wykres liniowy,
- heatmapę,
- kod JavaScript odpowiedzialny za wizualizację danych.

Dodatkowo w:

```text
app/__init__.py
```

zarejestrowałam Blueprint dashboardu:

```python
from app.routes.dashboard import dashboard_bp

app.register_blueprint(
    dashboard_bp
)
```

Bez rejestracji Blueprintu endpoint:

```text
/dashboard
```

zwracał błąd:

```text
404 Not Found
```

Po zarejestrowaniu Blueprintu endpoint został poprawnie udostępniony przez Flask.

---

# 15. Test działania

Aplikację uruchomiłam poleceniem:

```powershell
python run.py
```

Następnie otworzyłam:

```text
http://127.0.0.1:5000/dashboard
```

Dashboard został poprawnie wyświetlony.

---

# 16. Rezultat

Dashboard wyświetla wszystkie trzy elementy wymagane w zadaniu.

## 1. Wykres kołowy

Pokazuje rozkład rezerwacji według departamentów:

```text
HR
Marketing
IT
```

## 2. Heatmapa

Pokazuje liczbę rezerwacji w macierzy:

```text
dzień tygodnia × godzina
```

Godziny są przedstawione w zakresie:

```text
8:00 – 18:00
```

Im większa liczba rezerwacji, tym intensywniejszy kolor komórki.

## 3. Trend

Pokazuje liczbę rezerwacji dla każdego dnia z ostatnich 30 dni.

Uwzględnione są również dni, w których liczba rezerwacji wynosi:

```text
0
```

---

# Wnioski

W zadaniu wykorzystałam agregację danych po stronie PostgreSQL za pomocą SQLAlchemy.

Najważniejsze użyte funkcje to:

```python
func.count()
```

do liczenia rezerwacji,

```python
func.extract('dow', ...)
```

do pobierania dnia tygodnia,

```python
func.extract('hour', ...)
```

do pobierania godziny,

oraz:

```python
func.date()
```

do grupowania rezerwacji według daty.

Dane pobrane przez Flask zostały przekazane do szablonu Jinja, zamienione na JSON, a następnie wykorzystane przez JavaScript.

Do wizualizacji wykresu kołowego i trendu wykorzystałam bibliotekę Chart.js.

Heatmapa została zbudowana jako tabela HTML, w której intensywność koloru komórki zależy od liczby rezerwacji.

## Oczekiwany rezultat

Dashboard zawiera:

- wykres kołowy rezerwacji według departamentu,
- heatmapę popularności godzin,
- wykres trendu rezerwacji z ostatnich 30 dni.
