Zadanie 10 – Aplikacja do rejestracji na wydarzenie

  Stwórz kompletną mini-aplikację.

  a. Zdefiniuj model SQLAlchemy Registration z polami id, name (string), email (string, unikalny).

  b. Stwórz ścieżkę /register, która będzie obsługiwać metody GET i POST (poszukaj w dokumentacji Flaska, jak to zrobić - methods=['GET', 'POST']).

  c. Stwórz szablon register.html z formularzem HTML (<form>) zawierającym pola na imię i email oraz przycisk "Zarejestruj". Formularz powinien wysyłać dane metodą POST.

  d. W funkcji dla ścieżki /register, sprawdź, czy żądanie jest typu POST. Jeśli tak, pobierz dane z formularza, stwórz nowy obiekt Registration, zapisz go w bazie danych i przekieruj użytkownika na stronę z podziękowaniem. Jeśli żądanie jest typu GET, po prostu wyświetl formularz.


# Zadanie 10 – Aplikacja do rejestracji na wydarzenie

## Co zrobiłam?

Stworzyłam osobną mini-aplikację Flask służącą do rejestracji użytkowników na wydarzenie.

Aplikacja:

- wyświetla formularz rejestracyjny,
- przyjmuje imię i adres email,
- obsługuje żądania GET i POST,
- zapisuje dane użytkownika w bazie PostgreSQL,
- po poprawnym zapisie przekierowuje użytkownika na stronę z podziękowaniem.

Zadanie 10 zrobiłam jako osobną aplikację, niezależną od wcześniejszych zadań.

Struktura projektu wygląda następująco:

```text
zad10/
│
├── app.py
│
└── templates/
    ├── register.html
    └── thank_you.html
```

---

## 1. Utworzenie aplikacji Flask

W pliku `app.py` utworzyłam nową aplikację:

```python
app = Flask(__name__)
```

`Flask(__name__)` tworzy obiekt aplikacji Flask.

---

## 2. Połączenie z PostgreSQL

Do obsługi bazy danych wykorzystałam Flask-SQLAlchemy:

```python
from flask_sqlalchemy import SQLAlchemy
```

Następnie skonfigurowałam połączenie z osobną bazą:

```text
rejestracja_db
```

i połączyłam SQLAlchemy z aplikacją:

```python
db = SQLAlchemy(app)
```

Dzięki temu mogę pracować z bazą PostgreSQL za pomocą klas i obiektów Pythona.

---

## 3. Model `Registration`

Stworzyłam model:

```python
class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

Model `Registration` reprezentuje tabelę:

```text
registration
```

w bazie PostgreSQL.

### Pole `id`

```python
id = db.Column(db.Integer, primary_key=True)
```

`id` jest kluczem głównym.

Każda rejestracja otrzymuje własny identyfikator.

### Pole `name`

```python
name = db.Column(db.String(100), nullable=False)
```

Przechowuje imię użytkownika.

`nullable=False` oznacza, że wartość nie może być `NULL`.

### Pole `email`

```python
email = db.Column(db.String(120), unique=True, nullable=False)
```

Przechowuje adres email.

`unique=True` oznacza, że ten sam email nie może zostać zapisany w tabeli więcej niż jeden raz.

`nullable=False` oznacza, że email jest wymagany.

---

## 4. Utworzenie tabeli w PostgreSQL

Po zdefiniowaniu modelu utworzyłam tabelę za pomocą:

```python
from app import app, db

with app.app_context():
    db.create_all()
```

`app.app_context()` tworzy kontekst aplikacji potrzebny SQLAlchemy do pracy z konfiguracją Flaska.

```python
db.create_all()
```

tworzy w bazie tabele odpowiadające modelom, jeżeli jeszcze nie istnieją.

Po wykonaniu polecenia w bazie `rejestracja_db` powstała tabela:

```text
registration
```

z kolumnami:

```text
id
name
email
```

---

## 5. Ścieżka `/register`

Stworzyłam ścieżkę:

```python
@app.route('/register', methods=['GET', 'POST'])
def register():
```

Ta sama ścieżka obsługuje dwie metody HTTP:

```text
GET
POST
```

### GET

GET jest używany, kiedy użytkownik wchodzi na:

```text
/register
```

Wtedy Flask wykonuje:

```python
return render_template('register.html')
```

i wyświetla formularz.

Można to zapamiętać jako:

```text
GET → chcę otrzymać stronę/formularz
```

### POST

POST jest używany, kiedy użytkownik wypełnia formularz i klika przycisk:

```text
Zarejestruj
```

Formularz wysyła wtedy dane do serwera.

Można to zapamiętać jako:

```text
POST → wysyłam dane do serwera
```

---

## 6. Formularz HTML

W `register.html` stworzyłam formularz:

```html
<form method="POST">

    <label for="name">Imię:</label>
    <input type="text" id="name" name="name" required>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>

    <button type="submit">Zarejestruj</button>

</form>
```

Najważniejszy fragment:

```html
<form method="POST">
```

oznacza, że formularz wysyła dane metodą POST.

Atrybuty:

```html
name="name"
name="email"
```

są szczególnie ważne, ponieważ Flask wykorzystuje je później do pobrania wartości z formularza.

---

## 7. Sprawdzenie rodzaju żądania

W funkcji `register()` użyłam:

```python
if request.method == 'POST':
```

Sprawdzam w ten sposób, czy użytkownik właśnie wysłał formularz.

Jeżeli warunek jest prawdziwy, rozpoczyna się obsługa przesłanych danych.

Jeżeli użytkownik tylko wszedł na stronę, żądanie jest typu GET i formularz zostaje po prostu wyświetlony.

---

## 8. Pobranie danych z formularza

Dane pobieram za pomocą:

```python
name = request.form['name']
email = request.form['email']
```

`request.form` zawiera dane przesłane przez formularz HTML.

Klucze:

```python
'name'
'email'
```

odpowiadają wartościom `name=""` w HTML:

```html
<input name="name">
<input name="email">
```

Czyli połączenie wygląda tak:

```text
HTML:

name="name"
      ↓
request.form['name']


name="email"
      ↓
request.form['email']
```

---

## 9. Utworzenie obiektu `Registration`

Na podstawie pobranych danych tworzę nowy obiekt:

```python
new_registration = Registration(
    name=name,
    email=email
)
```

Na tym etapie istnieje już obiekt Pythona, ale dane nie są jeszcze zapisane na stałe w PostgreSQL.

---

## 10. Zapis do bazy

Najpierw dodaję obiekt do sesji SQLAlchemy:

```python
db.session.add(new_registration)
```

Następnie zatwierdzam zmianę:

```python
db.session.commit()
```

Można to zapamiętać tak:

```text
db.session.add()
        ↓
przygotuj obiekt do zapisania

db.session.commit()
        ↓
zatwierdź i zapisz zmianę w bazie
```

Po `commit()` rekord znajduje się już w tabeli `registration`.

---

## 11. Przekierowanie użytkownika

Po zapisaniu danych wykonuję:

```python
return redirect(url_for('thank_you'))
```

`url_for('thank_you')` tworzy adres prowadzący do funkcji:

```python
def thank_you():
```

Natomiast:

```python
redirect(...)
```

przekierowuje użytkownika pod ten adres.

---

## 12. Strona podziękowania

Stworzyłam osobną ścieżkę:

```python
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')
```

Po poprawnym wysłaniu formularza użytkownik zostaje przekierowany na:

```text
/thank-you
```

gdzie wyświetla się komunikat:

```text
Dziękujemy za rejestrację!
```

---

## 13. Test aplikacji

Uruchomiłam aplikację:

```powershell
python app.py
```

Następnie weszłam na:

```text
http://127.0.0.1:5000/register
```

Po wejściu na stronę Flask obsłużył żądanie:

```text
GET /register → 200
```

Po wypełnieniu formularza i kliknięciu `Zarejestruj`:

```text
POST /register → 302
```

Kod `302` oznacza przekierowanie.

Następnie przeglądarka została przekierowana na:

```text
GET /thank-you → 200
```

Kod `200` oznacza, że żądanie zostało poprawnie obsłużone.

---

## 14. Sprawdzenie danych w pgAdmin

Po wysłaniu formularza sprawdziłam tabelę:

```text
rejestracja_db
→ Schemas
→ public
→ Tables
→ registration
```

Dane przesłane przez formularz zostały poprawnie zapisane w PostgreSQL.

Oznacza to, że formularz nie tylko wyświetla stronę, ale faktycznie komunikuje się z backendem i bazą danych.

---

# Cały przepływ aplikacji

Najważniejszy mechanizm tego zadania wygląda tak:

```text
Użytkownik wchodzi na /register
            ↓
      GET /register
            ↓
     Flask uruchamia
       register()
            ↓
render_template('register.html')
            ↓
   wyświetlenie formularza
            ↓
 użytkownik wpisuje dane
            ↓
     klik "Zarejestruj"
            ↓
      POST /register
            ↓
 request.method == 'POST'
            ↓
       request.form
            ↓
    pobranie name/email
            ↓
 Registration(name, email)
            ↓
   db.session.add()
            ↓
  db.session.commit()
            ↓
       PostgreSQL
            ↓
 tabela registration
            ↓
        redirect()
            ↓
       /thank-you
            ↓
"Dziękujemy za rejestrację!"
```

# Do zapamiętania

`GET` służy tutaj do pobrania i wyświetlenia formularza.

`POST` służy do wysłania danych formularza do serwera.

`request.method` pozwala sprawdzić metodę żądania.

`request.form` pozwala pobrać dane przesłane przez formularz.

`Registration(...)` tworzy nowy obiekt modelu.

`db.session.add()` dodaje obiekt do sesji SQLAlchemy.

`db.session.commit()` zapisuje zmianę w bazie danych.

`redirect()` przekierowuje użytkownika.

`url_for()` tworzy adres na podstawie nazwy funkcji widoku.

Najważniejsza rzecz z tego zadania:

```text
HTML formularz
      ↓
Flask
      ↓
SQLAlchemy
      ↓
PostgreSQL
      ↓
redirect
      ↓
HTML
```

Czyli stworzyłam kompletny przepływ danych od formularza w przeglądarce, przez backend Flaska, aż do zapisu danych w bazie PostgreSQL.