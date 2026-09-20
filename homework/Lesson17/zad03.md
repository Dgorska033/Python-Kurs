Zadanie 3 – Przekaż listę do szablonu
W pliku app.py stwórz listę swoich ulubionych filmów. Następnie stwórz nową ścieżkę
/movies i szablon movies.html. Przekaż listę filmów do szablonu i wyświetl ją jako listę
nieuporządkowaną (
) w HTML.

## Co zrobiłam?

Stworzyłam w Pythonie listę zawierającą moje ulubione filmy.

Następnie dodałam nową ścieżkę `/movies`, która uruchamia funkcję `movies()`.

Funkcja używa `render_template()`, aby:
- otworzyć szablon `movies.html`,
- przekazać do niego listę filmów,
- umożliwić wykorzystanie danych z Pythona w kodzie HTML.

## Kod dodany do `app1.py`

```python
ulubione_filmy = [
    "John Wick",
    "Spiderman",
    "Diuna"
]

@app.route('/movies')
def movies():
    return render_template('movies.html', movies=ulubione_filmy)
```

## Przekazywanie danych do HTML

W:

```python
render_template('movies.html', movies=ulubione_filmy)
```

`ulubione_filmy` to lista istniejąca w Pythonie.

`movies` to nazwa, pod którą ta lista jest dostępna w szablonie `movies.html`.

Czyli:

`ulubione_filmy` w Pythonie → `movies` w HTML.

## Kod w `templates/movies.html`

```html
<h1>Moje ulubione filmy</h1>

<ul>
    {% for film in movies %}
        <li>{{ film }}</li>
    {% endfor %}
</ul>
```

## Jak działa pętla?

```html
{% for film in movies %}
```

Jest to pętla Jinja, która przechodzi po wszystkich elementach listy `movies`.

Działa podobnie do pętli Pythona:

```python
for film in movies:
```

Natomiast:

```html
{{ film }}
```

wyświetla aktualny element listy.

`<ul>` tworzy listę nieuporządkowaną w HTML, a `<li>` oznacza pojedynczy element tej listy.

## Test

Po uruchomieniu aplikacji wchodzę na:

`http://127.0.0.1:5000/movies`

Flask uruchamia funkcję `movies()`, przekazuje listę do `movies.html`, a Jinja generuje z niej listę filmów na stronie.

## Do zapamiętania

Przepływ danych wygląda tak:

`lista w Pythonie → render_template() → zmienna w Jinja → HTML → przeglądarka`