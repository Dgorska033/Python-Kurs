from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Konfiguracja połączenia z bazą danych
# Format: postgresql://uzytkownik:haslo@host:port/nazwa_bazy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mama.123@localhost:5432/moja_baza'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Wyłączenie niepotrzebnej funkcji śledzenia

# Inicjalizacja obiektu SQLAlchemy
db = SQLAlchemy(app)

# Definicja modelu (tabeli) za pomocą klasy
# Dziedziczymy po db.Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Metoda __repr__ definiuje, jak obiekt będzie wyglądał po wydrukowaniu
    def __repr__(self):
        return f'<User {self.username}>'

@app.route('/')
def index():
    # Pobieranie wszystkich użytkowników z bazy
    # User.query.all() to odpowiednik "SELECT * FROM user;"
    users = User.query.all()
    return render_template('index.html', users=users)

# Aby stworzyć tabele w bazie danych na podstawie modeli,
# musisz otworzyć terminal Pythona i wykonać:
# from app import db
# db.create_all()
# Zrób to tylko raz!

# Zadanie 1 – Strona "O mnie"
# Po wejściu na adres /me Flask uruchomi funkcję me()
@app.route('/me')
def me():
    return 'Dominika Górska'

# Zadanie 2 – Prosty kalkulator
# <int:num1> i <int:num2> pobierają dwie liczby całkowite z adresu URL
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    suma = num1 + num2
    return f'Wynik to: {suma}'

# w pasku przeglądarki trzeba dopisać np. add/5/8 

ulubione_filmy = [
    "John Wick",
    "Spiderman",
    "Diuna"]

# Zadanie 3 – Przekazanie listy filmów do szablonu
@app.route('/movies')
def movies():
    page_title = "Moje ulubione filmy"

    return render_template(
        'movies.html',
        movies=ulubione_filmy,
        page_title=page_title
    )

ksiazka = {
    'title': 'Hobbit',
    'author': 'J.R.R. Tolkien',
    'year': 1937}

# Zadanie 6 – Słownik w szablonie
@app.route('/book')
def book():
    return render_template('book.html', book=ksiazka)

galeria = [
    {
        'url': 'funny.jpg',
        'caption': 'Coś co znalazłam w parku. Nie umiem określić ale jest zabawne'
    },
    {
        'url': 'islandia.jpg',
        'caption': 'Mam fajną fotkę taką'
    },
    {
        'url': 'widok.jpg',
        'caption': 'To też moja fotka widoku'
    }
]

# Zadanie 7 – Prosta galeria
@app.route('/gallery')
def gallery():
    return render_template('gallery.html', images=galeria)


# Zadanie 8 – Model produktu w SQLAlchemy

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'


# Zadanie 9 – Wyświetlanie produktów

@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)




if __name__ == '__main__':
    app.run(debug=True)

