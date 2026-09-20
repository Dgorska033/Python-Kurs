Zadanie 5 – Kolorowanie listy

 W szablonie movies.html z zadania 3, użyj pętli for oraz instrukcji if w Jinja2,
aby co drugi element listy miał inny kolor tła. Możesz użyć właściwości loop.index w pętli.

# Zadanie 5 – Kolorowanie listy

## Co zrobiłam?

Zmodyfikowałam szablon `movies.html` z poprzedniego zadania.

W pętli `for` dodałam instrukcję `if`, która sprawdza numer aktualnego elementu listy.

Dzięki temu co drugi film otrzymuje inny kolor tła.

## Kod w `movies.html`

```html
<ul>
    {% for film in movies %}

        {% if loop.index % 2 == 0 %}
            <li style="background-color: lightgray;">{{ film }}</li>
        {% else %}
            <li>{{ film }}</li>
        {% endif %}

    {% endfor %}
</ul>
```

## Jak działa `loop.index`?

`loop.index` w Jinja przechowuje numer aktualnego elementu pętli.

Numerowanie zaczyna się od 1:

- pierwszy film → `loop.index = 1`
- drugi film → `loop.index = 2`
- trzeci film → `loop.index = 3`
- czwarty film → `loop.index = 4`

## Jak sprawdzam co drugi element?

Użyłam warunku:

```html
{% if loop.index % 2 == 0 %}
```

Operator `%` zwraca resztę z dzielenia.

Jeżeli numer elementu jest podzielny przez 2 bez reszty, oznacza to, że jest parzysty.

Przykładowo:

`2 % 2 = 0` → element zostanie pokolorowany

`3 % 2 = 1` → element nie zostanie pokolorowany

`4 % 2 = 0` → element zostanie pokolorowany

Dlatego kolor otrzymują elementy 2, 4, 6 itd.

## Kolorowanie elementu

Do zmiany koloru tła użyłam CSS:

```html
style="background-color: lightgray;"
```

Jinja za pomocą `if` decyduje, **który element ma zostać pokolorowany**, a CSS `background-color` określa **jaki będzie jego kolor tła**.

## Do zapamiętania

W Jinja mogę używać instrukcji warunkowych podobnie jak w Pythonie:

```html
{% if warunek %}
    ...
{% else %}
    ...
{% endif %}
```

`loop.index` pozwala sprawdzić, który element pętli jest aktualnie wykonywany.