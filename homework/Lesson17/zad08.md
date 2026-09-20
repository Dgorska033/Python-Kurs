Zadanie 8 – Model produktu w SQLAlchemy

 Zdefiniuj model SQLAlchemy o nazwie Product. 
Powinien on zawierać pola: id (klucz główny, integer), name (string, nie może być pusty) oraz price (float, nie może być pusty). 
Następnie w interaktywnej konsoli Pythona dodaj kilka przykładowych produktów do bazy danych.

# Zadanie 8 – Model produktu w SQLAlchemy

## Co zrobiłam?

Stworzyłam nowy model SQLAlchemy o nazwie `Product`.

Model reprezentuje tabelę produktów w bazie danych i posiada trzy pola:

- `id` – identyfikator produktu i klucz główny,
- `name` – nazwa produktu,
- `price` – cena produktu.

## Model `Product`

W `app1.py` dodałam:

```python
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Product {self.name}>'
```

## Znaczenie poszczególnych pól

```python
id = db.Column(db.Integer, primary_key=True)
```

`db.Integer` oznacza liczbę całkowitą.

`primary_key=True` ustawia `id` jako klucz główny tabeli. Dzięki temu każdy produkt posiada własny identyfikator.

---

```python
name = db.Column(db.String(100), nullable=False)
```

`db.String(100)` przechowuje tekst o maksymalnej długości 100 znaków.

`nullable=False` oznacza, że kolumna nie może posiadać wartości `NULL`.

---

```python
price = db.Column(db.Float, nullable=False)
```

`db.Float` pozwala przechowywać liczby zmiennoprzecinkowe, np. `89.99`.

`nullable=False` oznacza, że cena produktu jest wymagana.

## Utworzenie tabeli

W interaktywnej konsoli Pythona zaimportowałam aplikację i bazę:

```python
from app1 import app, db
```

Następnie utworzyłam tabelę na podstawie modelu:

```python
with app.app_context():
    db.create_all()
```

`db.create_all()` tworzy w bazie tabele dla modeli SQLAlchemy, które jeszcze nie istnieją.

`app.app_context()` udostępnia SQLAlchemy kontekst aplikacji Flask potrzebny do wykonania operacji na bazie.

## Dodanie przykładowych produktów

Zaimportowałam model:

```python
from app1 import Product
```

Następnie utworzyłam trzy obiekty:

```python
produkt1 = Product(name="Laptop", price=3500.00)
produkt2 = Product(name="Myszka", price=89.99)
produkt3 = Product(name="Klawiatura", price=199.99)
```

Na tym etapie obiekty zostały utworzone w Pythonie, ale nie były jeszcze zapisane w bazie.

## Zapisanie produktów do bazy

Produkty dodałam do sesji SQLAlchemy:

```python
with app.app_context():
    db.session.add_all([produkt1, produkt2, produkt3])
    db.session.commit()
```

`db.session.add_all()` dodaje kilka obiektów do sesji.

`db.session.commit()` zatwierdza zmiany i zapisuje produkty w bazie danych.

## Sprawdzenie danych

Sprawdziłam zapisane produkty za pomocą:

```python
with app.app_context():
    print(Product.query.all())
```

Otrzymałam:

```text
[<Product Laptop>, <Product Myszka>, <Product Klawiatura>]
```

Oznacza to, że wszystkie trzy produkty zostały poprawnie zapisane w bazie.

Dane można również zobaczyć w pgAdmin w tabeli:

`moja_baza → Schemas → public → Tables → product`

## Do zapamiętania

Proces dodawania danych za pomocą SQLAlchemy wyglądał następująco:

`model Product → db.create_all() → utworzenie obiektów → db.session.add_all() → db.session.commit() → dane w PostgreSQL`

Samo utworzenie:

```python
Product(name="Laptop", price=3500.00)
```

nie zapisuje jeszcze produktu w bazie.

Dopiero `db.session.commit()` zatwierdza zmiany w bazie danych.