Zadanie 2 – Prosty kalkulator
Utwórz ścieżkę /add/<int:num1>/<int:num2>. Funkcja przypisana do tej ścieżki powinna
przyjąć dwie liczby jako argumenty, zsumować je i zwrócić wynik w formacie "Wynik to:
[suma]".

## Co zrobiłam?

Dodałam do aplikacji Flask nową ścieżkę:

`/add/<int:num1>/<int:num2>`

- `<int:num1>` pobiera pierwszą liczbę całkowitą z adresu URL.
- `<int:num2>` pobiera drugą liczbę całkowitą z adresu URL.
- Flask przekazuje pobrane liczby jako argumenty `num1` i `num2` do funkcji `add()`.
- W funkcji dodaję obie liczby i zapisuję wynik w zmiennej `suma`.
- Za pomocą `return` zwracany jest napis zawierający wynik działania.

## Kod dodany do `app1.py`

```python
@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    suma = num1 + num2
    return f'Wynik to: {suma}'


Przykład działania

Dla adresu:

http://127.0.0.1:5000/add/5/8

Flask odczytuje:

num1 = 5
num2 = 8

i wyświetla:

Wynik to: 13