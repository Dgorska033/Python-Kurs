Zadanie 6 – Słownik w szablonie

Stwórz w app.py słownik opisujący książkę, np. {'title': 'Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937}. 
Stwórz ścieżkę /book i szablon book.html. 
Przekaż słownik do szablonu i wyświetl jego zawartość w czytelny sposób, np. używając nagłówków i paragrafów.

## Co zrobiłam?

Stworzyłam w Pythonie słownik `ksiazka`, który przechowuje informacje o książce:

```python
ksiazka = {
    'title': 'Hobbit',
    'author': 'J.R.R. Tolkien',
    'year': 1937
}
```

Słownik zawiera trzy pary klucz–wartość:

- `title` → tytuł książki
- `author` → autor książki
- `year` → rok wydania

## Utworzenie ścieżki `/book`

Dodałam nową ścieżkę Flask:

```python
@app.route('/book')
def book():
    return render_template('book.html', book=ksiazka)
```

Po wejściu na `/book` Flask uruchamia funkcję `book()`.

Funkcja otwiera szablon `book.html` i przekazuje do niego słownik `ksiazka`.

## Przekazywanie słownika do szablonu

W:

```python
render_template('book.html', book=ksiazka)
```

`ksiazka` to słownik znajdujący się w Pythonie.

`book` to nazwa, pod którą słownik jest dostępny w szablonie HTML.

Czyli:

`ksiazka` w Pythonie → `book` w Jinja/HTML.

## Kod w `book.html`

```html
<h1>{{ book.title }}</h1>

<p>Autor: {{ book.author }}</p>
<p>Rok wydania: {{ book.year }}</p>
```

Za pomocą Jinja pobieram konkretne wartości ze słownika:

`{{ book.title }}` → Hobbit

`{{ book.author }}` → J.R.R. Tolkien

`{{ book.year }}` → 1937

## Różnica względem listy z poprzednich zadań

Przy liście filmów używałam pętli `for`, ponieważ chciałam przejść po wszystkich elementach listy.

Tutaj mam słownik i chcę wyświetlić konkretne informacje, dlatego odwołuję się bezpośrednio do jego wartości:

```html
{{ book.title }}
{{ book.author }}
{{ book.year }}
```

## Do zapamiętania

Flask może przekazywać do szablonów różne typy danych, np. listy i słowniki.

Przepływ danych w tym zadaniu:

`Słownik w Pythonie → render_template() → Jinja → HTML → przeglądarka`