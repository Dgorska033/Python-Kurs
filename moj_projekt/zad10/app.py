# Importujemy elementy potrzebne do działania aplikacji Flask.
# render_template - wyświetlanie szablonów HTML.
# request - pozwala sprawdzić rodzaj żądania i pobrać dane z formularza.
# redirect - przekierowuje użytkownika na inną stronę.
# url_for - tworzy adres URL na podstawie nazwy funkcji.
from flask import Flask, render_template, request, redirect, url_for

# SQLAlchemy pozwala połączyć aplikację Flask z bazą danych
# i pracować z tabelami za pomocą klas i obiektów Pythona.
from flask_sqlalchemy import SQLAlchemy

# quote_plus pozwala bezpiecznie umieścić hasło w adresie połączenia.
# Jest to szczególnie ważne, jeśli hasło zawiera znaki specjalne.
from urllib.parse import quote_plus


# Tworzymy aplikację Flask.
app = Flask(__name__)


# ==========================================================
# Połączenie z bazą danych PostgreSQL
# ==========================================================

# Podajemy hasło użytkownika postgres.
# quote_plus() zamienia ewentualne znaki specjalne na format,
# który może być poprawnie użyty w adresie połączenia z bazą.
password = quote_plus("mama.123")


# Tworzymy adres połączenia z bazą danych.
#
# postgres       -> nazwa użytkownika PostgreSQL
# password       -> nasze zakodowane hasło
# localhost      -> baza działa na naszym komputerze
# rejestracja_db -> nazwa bazy utworzonej dla Zadania 10
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f'postgresql://postgres:{password}@localhost/rejestracja_db'
)


# Łączymy SQLAlchemy z naszą aplikacją Flask.
db = SQLAlchemy(app)

# ==========================================================
# Zadanie 10 – Model Registration
# ==========================================================

# Model Registration reprezentuje tabelę z osobami,
# które zarejestrowały się na wydarzenie.
class Registration(db.Model):

    # id jest kluczem głównym.
    # Każda rejestracja otrzyma własny, unikalny identyfikator.
    id = db.Column(db.Integer, primary_key=True)

    # name przechowuje imię użytkownika.
    # nullable=False oznacza, że wartość nie może być NULL.
    name = db.Column(db.String(100), nullable=False)

    # email przechowuje adres email.
    # unique=True oznacza, że ten sam email nie może pojawić się
    # w tabeli więcej niż jeden raz.
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Określamy, jak obiekt Registration ma być przedstawiany
    # np. podczas wyświetlania go w konsoli Pythona.
    def __repr__(self):
        return f'<Registration {self.email}>'


# ==========================================================
# Formularz rejestracji
# ==========================================================

# Ścieżka /register obsługuje dwie metody HTTP:
#
# GET  -> użytkownik wchodzi na stronę i otrzymuje formularz.
# POST -> użytkownik wysyła wypełniony formularz.
@app.route('/register', methods=['GET', 'POST'])
def register():

    # Sprawdzamy, czy formularz został wysłany metodą POST.
    if request.method == 'POST':

        # Pobieramy wartości przesłane z formularza HTML.
        # 'name' i 'email' odpowiadają atrybutom name=""
        # znajdującym się w polach <input> w register.html.
        name = request.form['name']
        email = request.form['email']

        # Tworzymy nowy obiekt modelu Registration
        # na podstawie danych otrzymanych z formularza.
        new_registration = Registration(
            name=name,
            email=email
        )

        # Dodajemy nową rejestrację do sesji SQLAlchemy.
        db.session.add(new_registration)

        # Zatwierdzamy zmiany - dopiero teraz rekord
        # zostaje zapisany w bazie PostgreSQL.
        db.session.commit()

        # Po poprawnym zapisie przekierowujemy użytkownika
        # do funkcji thank_you(), czyli na stronę podziękowania.
        return redirect(url_for('thank_you'))

    # Jeżeli żądanie było typu GET, nie zapisujemy niczego
    # do bazy - po prostu wyświetlamy formularz.
    return render_template('register.html')


# ==========================================================
# Strona podziękowania
# ==========================================================

# Ta strona zostanie wyświetlona po poprawnym
# wysłaniu i zapisaniu formularza.
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')


# ==========================================================
# Uruchomienie aplikacji
# ==========================================================

# Ten fragment uruchamia serwer Flask tylko wtedy,
# gdy app.py uruchamiamy bezpośrednio.
if __name__ == '__main__':
    app.run(debug=True)

