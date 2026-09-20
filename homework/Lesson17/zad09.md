Zadanie 9 – Wyświetlanie produktów

 Stwórz ścieżkę /products i szablon products.html.
 W funkcji pobierz wszystkie produkty z bazy danych (stworzone w zadaniu 8) i przekaż je do szablonu. Wyświetl produkty w tabeli HTML, 
 która będzie miała kolumny "Nazwa" i "Cena".

 # Zadanie 9 – Wyświetlanie produktów

## Co zrobiłam?

Stworzyłam nową ścieżkę `/products`, która pobiera wszystkie produkty zapisane wcześniej w bazie danych.

Następnie przekazałam pobrane produkty do nowego szablonu `products.html`.

W szablonie wykorzystałam pętlę Jinja, aby przejść po wszystkich produktach i wyświetlić ich nazwy oraz ceny w tabeli HTML.

## Ścieżka `/products`

W pliku `app1.py` dodałam:

```python
@app.route('/products')
def products():
    products = Product.query.all()
    return render_template('products.html', products=products)
```

Po wejściu w przeglądarce na:

```text
http://127.0.0.1:5000/products
```

Flask uruchamia funkcję `products()`.

## Pobieranie produktów z bazy danych

Do pobrania produktów użyłam:

```python
products = Product.query.all()
```

`Product` jest modelem SQLAlchemy utworzonym w Zadaniu 8.

```python
Product.query
```

tworzy zapytanie dotyczące modelu `Product`.

Natomiast:

```python
.all()
```

pobiera wszystkie rekordy znajdujące się w tabeli `product`.

W mojej bazie znajdują się obecnie:

- Laptop
- Myszka
- Klawiatura

Czyli:

```python
products = Product.query.all()
```

zwraca kolekcję obiektów `Product` reprezentujących rekordy zapisane w PostgreSQL.

## Przekazanie produktów do szablonu

Następnie użyłam:

```python
return render_template('products.html', products=products)
```

Pierwsze:

```python
'products.html'
```

określa szablon HTML, który Flask ma wyświetlić.

Natomiast:

```python
products=products
```

przekazuje pobrane produkty do szablonu.

Po lewej stronie `products` jest nazwą dostępną w Jinja.

Po prawej stronie `products` jest zmienną z Pythona zawierającą produkty pobrane z bazy.

Przepływ wygląda więc tak:

```text
PostgreSQL
    ↓
Product.query.all()
    ↓
products w Pythonie
    ↓
render_template()
    ↓
products w Jinja
```

## Utworzenie `products.html`

W folderze `templates` utworzyłam nowy plik:

```text
templates/
└── products.html
```

W szablonie stworzyłam tabelę HTML:

```html
<table border="1">
    <tr>
        <th>Nazwa</th>
        <th>Cena</th>
    </tr>

    {% for product in products %}
    <tr>
        <td>{{ product.name }}</td>
        <td>{{ product.price }} zł</td>
    </tr>
    {% endfor %}

</table>
```

## Budowa tabeli HTML

Do utworzenia tabeli użyłam:

```html
<table>
```

Znacznik `<table>` oznacza całą tabelę.

Każdy wiersz tabeli tworzony jest za pomocą:

```html
<tr>
```

Nagłówki kolumn utworzyłam za pomocą:

```html
<th>Nazwa</th>
<th>Cena</th>
```

`<th>` oznacza komórkę nagłówkową tabeli.

Dane produktów wyświetlam natomiast za pomocą:

```html
<td>
```

`<td>` oznacza zwykłą komórkę zawierającą dane.

## Pętla Jinja

Produkty pobrane z bazy znajdują się w `products`.

Dlatego użyłam:

```html
{% for product in products %}
```

Pętla przechodzi kolejno po wszystkich produktach.

W każdym obrocie pętli zmienna:

```text
product
```

oznacza jeden konkretny obiekt modelu `Product`.

Dzięki temu mogę odwołać się do jego pól.

## Wyświetlenie nazwy produktu

Do wyświetlenia nazwy użyłam:

```html
{{ product.name }}
```

`name` odpowiada polu zdefiniowanemu wcześniej w modelu:

```python
name = db.Column(db.String(100), nullable=False)
```

## Wyświetlenie ceny produktu

Do wyświetlenia ceny użyłam:

```html
{{ product.price }} zł
```

`price` odpowiada polu modelu:

```python
price = db.Column(db.Float, nullable=False)
```

Dodatkowo po wartości ceny wyświetlam tekst `zł`.

## Jak powstają kolejne wiersze?

Dla każdego produktu pętla wykonuje:

```html
<tr>
    <td>{{ product.name }}</td>
    <td>{{ product.price }} zł</td>
</tr>
```

Jeżeli w bazie są trzy produkty, pętla wykona ten fragment trzy razy.

W rezultacie otrzymuję tabelę:

| Nazwa | Cena |
|---|---:|
| Laptop | 3500.0 zł |
| Myszka | 89.99 zł |
| Klawiatura | 199.99 zł |

Nie muszę wpisywać każdego produktu ręcznie do HTML.

Jeżeli później dodam kolejny produkt do bazy, zostanie on również pobrany przez:

```python
Product.query.all()
```

i pętla Jinja utworzy dla niego kolejny wiersz tabeli.

## Do zapamiętania

W tym zadaniu połączyłam bazę danych, SQLAlchemy, Flask, Jinja i HTML.

Cały przepływ danych wygląda tak:

```text
PostgreSQL
    ↓
model Product
    ↓
Product.query.all()
    ↓
lista produktów
    ↓
render_template()
    ↓
products.html
    ↓
pętla Jinja
    ↓
tabela HTML
    ↓
przeglądarka
```

`Product.query.all()` pobiera wszystkie produkty z bazy.

`render_template()` przekazuje je do szablonu.

Pętla Jinja przechodzi po produktach.

`product.name` i `product.price` pozwalają odczytać dane konkretnego produktu.

Najważniejsze jest to, że dane wyświetlane na stronie nie są wpisane na stałe w HTML – pochodzą bezpośrednio z bazy danych.