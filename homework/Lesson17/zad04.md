Zadanie 4 – Dynamiczny tytuł strony
Zmodyfikuj zadanie 3. Oprócz listy filmów, przekaż do szablonu movies.html 
również zmienną page_title z wartością "Moje ulubione filmy".
Użyj tej zmiennej w znaczniku <title> w szablonie.

## Co zmieniłam względem Zadania 3?

W Zadaniu 3 tytuł strony był wpisany bezpośrednio w kodzie HTML.

W Zadaniu 4 stworzyłam zmienną `page_title` w Pythonie:

```python
page_title = "Moje ulubione filmy"
```

Następnie przekazałam ją do szablonu `movies.html` za pomocą `render_template()`.

## Kod w `app1.py`

```python
@app.route('/movies')
def movies():
    page_title = "Moje ulubione filmy"

    return render_template(
        'movies.html',
        movies=ulubione_filmy,
        page_title=page_title
    )
```

Do szablonu przekazuję teraz dwie zmienne:

- `movies` – zawiera listę moich ulubionych filmów,
- `page_title` – zawiera tytuł strony.

## Zmiana w `movies.html`

Zamiast wpisywać tytuł na sztywno:

```html
<title>Moje ulubione filmy</title>
```

użyłam zmiennej przekazanej z Pythona:

```html
<title>{{ page_title }}</title>
```

Mogę użyć tej samej zmiennej również jako nagłówka strony:

```html
<h1>{{ page_title }}</h1>
```

## Jak to działa?

`page_title` powstaje w Pythonie:

```python
page_title = "Moje ulubione filmy"
```

Następnie `render_template()` przekazuje ją do `movies.html`:

```python
page_title=page_title
```

A Jinja wstawia jej wartość do HTML:

```html
{{ page_title }}
```

Czyli przepływ wygląda tak:

`Python → render_template() → Jinja → HTML`

## Do zapamiętania

`{{ ... }}` w Jinja służy do wyświetlania wartości zmiennej w HTML.

Dzięki temu tytuł nie musi być wpisany na stałe w `movies.html` – może zostać przekazany dynamicznie z aplikacji Flask.