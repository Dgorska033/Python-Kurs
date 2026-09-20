# Zadanie 1 – Konfiguracja środowiska 

## Treść zadania

1. Zainstaluj PostgreSQL na swoim systemie.
2. Utwórz bazę danych `room_booking`.
3. Skonfiguruj plik `.env` z poprawnym connection string.
4. Uruchom aplikację i sprawdź endpoint `/test-db`.

**Oczekiwany rezultat:**  
Aplikacja łączy się z bazą danych i wyświetla komunikat:

`Połączenie OK!`

---

## 1. Sprawdzenie PostgreSQL

PostgreSQL był już zainstalowany na komputerze.

Sprawdziłam jego wersję poleceniem:

```powershell
& "C:\Program Files\PostgreSQL\17\bin\psql.exe" --version
```

Otrzymany wynik:

```text
psql (PostgreSQL) 17.11
```

Początkowo polecenie:

```powershell
psql --version
```

nie działało, ponieważ katalog zawierający `psql.exe` nie był dodany do zmiennej środowiskowej `PATH`.

Dlatego do uruchomienia programu użyłam pełnej ścieżki do `psql.exe`.

---

## 2. Utworzenie bazy danych `room_booking`

Uruchomiłam konsolę PostgreSQL za pomocą polecenia:

```powershell
& "C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres
```

Następnie utworzyłam bazę danych:

```sql
CREATE DATABASE room_booking;
```

PostgreSQL potwierdził wykonanie operacji:

```text
CREATE DATABASE
```

Poprawność utworzenia bazy sprawdziłam poleceniem:

```sql
\l
```

Na liście baz danych pojawiła się baza:

```text
room_booking
```

Po zakończeniu pracy z konsolą PostgreSQL wyszłam z niej poleceniem:

```sql
\q
```

---

## 3. Konfiguracja pliku `.env`

W głównym katalogu projektu utworzyłam plik:

```text
.env
```

W pliku zapisałam zmienną `DATABASE_URL` zawierającą connection string do PostgreSQL:

```env
DATABASE_URL=postgresql://postgres:TWOJE_HASLO@localhost:5432/room_booking
```

Connection string składa się z:

- `postgres` – nazwy użytkownika PostgreSQL,
- `TWOJE_HASLO` – hasła użytkownika,
- `localhost` – adresu lokalnego serwera PostgreSQL,
- `5432` – domyślnego portu PostgreSQL,
- `room_booking` – nazwy bazy danych.

Prawdziwe hasło znajduje się wyłącznie w lokalnym pliku `.env` i nie jest umieszczane w dokumentacji ani repozytorium Git.

Plik `.env` powinien znajdować się w `.gitignore`, ponieważ zawiera dane dostępowe do bazy.

---

## 4. Instalacja wymaganych bibliotek

Projekt posiadał już biblioteki Flask, Flask-SQLAlchemy oraz SQLAlchemy.

Do obsługi PostgreSQL oraz pliku `.env` potrzebne były dodatkowo:

```text
psycopg2-binary
python-dotenv
```

Zainstalowałam je poleceniem:

```powershell
pip install psycopg2-binary python-dotenv
```

Następnie zaktualizowałam plik `requirements.txt`.

W projekcie znajdują się między innymi:

```text
Flask==3.1.3
Flask-SQLAlchemy==3.1.1
psycopg2-binary==2.9.12
python-dotenv==1.2.3
SQLAlchemy==2.0.52
```

Biblioteka `psycopg2-binary` umożliwia aplikacji Python komunikację z bazą PostgreSQL.

Biblioteka `python-dotenv` umożliwia wczytywanie zmiennych środowiskowych zapisanych w pliku `.env`.

---

## 5. Konfiguracja aplikacji

W pliku `config.py` dodałam obsługę pliku `.env`:

```python
import os
from dotenv import load_dotenv

# Wczytanie zmiennych środowiskowych z pliku .env
load_dotenv()


class Config:
    # Pobranie connection string z pliku .env
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

    # Wyłączenie zbędnego śledzenia zmian SQLAlchemy
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

Dzięki temu dane potrzebne do połączenia z bazą nie są zapisane bezpośrednio w kodzie aplikacji.

Connection string jest pobierany ze zmiennej środowiskowej:

```python
os.getenv("DATABASE_URL")
```

---

## 6. Konfiguracja SQLAlchemy

W pliku `app/__init__.py` znajduje się wspólny obiekt SQLAlchemy:

```python
db = SQLAlchemy()
```

Jest on następnie inicjalizowany dla aplikacji Flask:

```python
db.init_app(app)
```

Modele korzystają z tego samego obiektu poprzez:

```python
from app import db
```

Dzięki temu konfiguracja aplikacji i wszystkie modele korzystają z jednej instancji SQLAlchemy.

---

## 7. Endpoint `/test-db`

Do aplikacji został dodany endpoint służący do sprawdzania połączenia z bazą danych:

```python
@app.route("/test-db")
def test_db():
    try:
        db.session.execute(text("SELECT 1"))
        return "Połączenie OK!"
    except Exception as e:
        return f"Błąd połączenia: {e}", 500
```

Do sprawdzenia połączenia wykorzystywane jest proste zapytanie SQL:

```sql
SELECT 1
```

Zapytanie nie wymaga istnienia konkretnej tabeli. Jego poprawne wykonanie potwierdza, że aplikacja może komunikować się z PostgreSQL.

Jeżeli połączenie działa, endpoint zwraca:

```text
Połączenie OK!
```

Jeżeli wystąpi problem z połączeniem, endpoint zwróci komunikat błędu oraz kod HTTP `500`.

---

## 8. Uruchomienie aplikacji

Aplikację uruchomiłam poleceniem:

```powershell
python run.py
```

Podczas uruchamiania aplikacja połączyła się z bazą danych.

W terminalu pojawił się również komunikat:

```text
Baza już zawiera dane. Pomijam seeding.
```

Oznacza to, że aplikacja mogła odczytać istniejące dane z bazy.

Następnie otworzyłam w przeglądarce endpoint:

```text
http://127.0.0.1:5000/test-db
```

Aplikacja wyświetliła:

```text
Połączenie OK!
```

W terminalu serwera pojawiło się również:

```text
GET /test-db HTTP/1.1" 200
```

Kod HTTP `200` oznacza, że żądanie zostało poprawnie obsłużone.

---

## Rezultat

Konfiguracja środowiska zakończyła się poprawnie.

Aplikacja:

1. korzysta z PostgreSQL,
2. łączy się z bazą `room_booking`,
3. pobiera connection string z pliku `.env`,
4. wykorzystuje Flask-SQLAlchemy do obsługi bazy,
5. poprawnie wykonuje zapytanie testowe do PostgreSQL,
6. zwraca kod HTTP `200` dla endpointu `/test-db`.

Endpoint:

```text
/test-db
```

zwraca oczekiwany komunikat:

```text
Połączenie OK!
```
