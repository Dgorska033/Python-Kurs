Zadanie 7 – Prosta galeria

Stwórz listę słowników, gdzie każdy słownik reprezentuje obrazek i zawiera klucze url 
(link do obrazka w internecie) i caption (podpis). 
Stwórz ścieżkę /gallery i szablon gallery.html.
Wyświetl wszystkie obrazki wraz z podpisami, używając pętli w Jinja2.

# Zadanie 7 – Prosta galeria

## Co zrobiłam?

Stworzyłam listę słowników `galeria`.

Każdy słownik reprezentuje jedno zdjęcie i zawiera:
- `url` – nazwę pliku ze zdjęciem,
- `caption` – podpis zdjęcia.

Przykładowy element:

```python
{
    'url': 'islandia.jpg',
    'caption': 'podpis'
}
```

## Własne zdjęcia

Zdjęcia umieściłam w folderze `static`, który we Flasku służy do przechowywania plików statycznych, np. zdjęć.

```text
moj_projekt/
├── app1.py
├── static/
│   ├── funny.jpg
│   ├── islandia.jpg
│   └── widok.jpg
└── templates/
    └── gallery.html
```

## Ścieżka `/gallery`

Dodałam ścieżkę:

```python
@app.route('/gallery')
def gallery():
    return render_template('gallery.html', images=galeria)
```

`images=galeria` przekazuje listę `galeria` z Pythona do szablonu pod nazwą `images`.

## Kod w `gallery.html`

```html
{% for image in images %}

    <img
        src="{{ url_for('static', filename=image.url) }}"
        alt="{{ image.caption }}"
        width="500"
    >

    <p>{{ image.caption }}</p>

{% endfor %}
```

## Jak działa pętla?

```html
{% for image in images %}
```

Pętla przechodzi po każdym słowniku znajdującym się na liście `images`.

W każdym obrocie pętli `image` oznacza jeden słownik.

Dlatego:

```html
{{ image.url }}
```

pobiera nazwę pliku zdjęcia, a:

```html
{{ image.caption }}
```

pobiera jego podpis.

## Jak wyświetlam własne zdjęcia?

Użyłam:

```html
src="{{ url_for('static', filename=image.url) }}"
```

`url_for()` tworzy poprawny adres do pliku znajdującego się w folderze `static`.

Na przykład dla:

```python
'url': 'islandia.jpg'
```

Flask utworzy ścieżkę do:

```text
/static/islandia.jpg
```

## Rozmiar zdjęć

Dodałam:

```html
width="500"
```

Ustawia to szerokość każdego zdjęcia na 500 pikseli.

Nie ustawiam wysokości, więc przeglądarka dopasowuje ją automatycznie i zachowuje oryginalne proporcje zdjęcia.

## Do zapamiętania

W tym zadaniu połączyłam:

`listę słowników → render_template() → pętlę Jinja → url_for() → własne zdjęcia z folderu static`

`templates` przechowuje szablony HTML, natomiast `static` może przechowywać zdjęcia i inne pliki statyczne.