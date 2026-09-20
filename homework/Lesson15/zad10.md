Zadanie 10 – Interaktywna edycja (dowolna aplikacja)
W wybranej przez siebie aplikacji (Raw SQL lub ORM) dodaj funkcję "Edytuj zadanie". Po
jej wybraniu, użytkownik powinien podać ID zadania, a następnie wpisać nowy opis.
Zaktualizuj odpowiedni wpis w bazie danych

Interaktywna edycja zadania (SQLAlchemy ORM)

W tym zadaniu aplikacja ORM została rozbudowana o możliwość edytowania opisu istniejącego zadania.

## Funkcja edytuj_zadanie()

W pliku `database.py` została dodana funkcja:

`edytuj_zadanie(id_zadania, nowy_opis)`

Funkcja odpowiada za znalezienie zadania o podanym ID oraz zmianę jego opisu.

Najpierw wyszukiwane jest zadanie:

`db.query(Zadanie).filter(Zadanie.id == id_zadania).first()`

Poszczególne elementy oznaczają:

`db.query(Zadanie)`
-> wybiera obiekty klasy `Zadanie`

`.filter(Zadanie.id == id_zadania)`
-> wyszukuje zadanie o konkretnym ID

`.first()`
-> pobiera pierwszy znaleziony obiekt lub zwraca `None`, jeśli zadanie nie istnieje


## Zmiana opisu

Jeśli zadanie zostało znalezione, jego opis jest zmieniany za pomocą:

`zadanie.opis = nowy_opis`

Ponieważ `zadanie` jest obiektem SQLAlchemy, możemy bezpośrednio zmienić wartość jego atrybutu.

Następnie wykonywane jest:

`db.commit()`

`commit()` zapisuje zmianę w bazie danych.


## Wartość zwracana

Jeśli zadanie zostało znalezione i zmienione, funkcja zwraca:

`True`

Jeśli zadanie o podanym ID nie istnieje, funkcja zwraca:

`False`

Dzięki temu `app_orm.py` może wyświetlić użytkownikowi odpowiedni komunikat.


## Zmiany w app_orm.py

Do menu została dodana opcja:

`Edytuj zadanie`

Po jej wybraniu użytkownik:

1. Podaje ID zadania, które chce edytować.
2. Podaje nowy opis zadania.
3. Program wywołuje `db.edytuj_zadanie()`.
4. Jeśli zadanie istnieje, nowy opis zostaje zapisany w bazie.
5. Jeśli zadanie nie istnieje, użytkownik otrzymuje odpowiedni komunikat.


## Obsługa błędnego ID

Konwersja ID została umieszczona w `try/except`.

Jeżeli użytkownik zamiast liczby poda np. tekst, `int()` zgłosi `ValueError`.

`except ValueError` przechwytuje ten wyjątek i wyświetla informację:

`Błędne ID. Podaj liczbę.`


## Najważniejsze

W SQLAlchemy ORM nie musimy ręcznie wykonywać zapytania SQL typu:

`UPDATE zadania SET opis = ...`

Zamiast tego pobieramy obiekt reprezentujący rekord:

`zadanie`

zmieniamy jego atrybut:

`zadanie.opis = nowy_opis`

i zapisujemy zmianę:

`db.commit()`

SQLAlchemy na podstawie zmiany obiektu generuje odpowiednie zapytanie `UPDATE` do bazy danych.