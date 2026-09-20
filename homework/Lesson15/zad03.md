 Zadanie 3 – Wyświetlanie ID
Zmodyfikuj funkcję pokaz_zadania w obu aplikacjach tak, aby oprócz opisu i statusu,
wyświetlała również ID każdego zadania. (W wersji ORM już to zrobiliśmy, upewnij się, że
wiesz dlaczego to działa)
Funkcja `pokaz_zadania()` została rozszerzona o wyświetlanie ID zadania oprócz jego opisu i statusu wykonania.

### Raw SQL

W wersji Raw SQL funkcja `pobierz_zadania()` wykonuje zapytanie:

`SELECT id, opis, zrobione FROM zadania`

SQLite zwraca każdy rekord jako krotkę w kolejności określonej w zapytaniu `SELECT`:

`(id, opis, zrobione)`

Dlatego do poszczególnych danych odwołujemy się za pomocą indeksów:

- `zadanie[0]` → ID zadania
- `zadanie[1]` → opis zadania
- `zadanie[2]` → status `zrobione`

Przykładowy rekord:

`(1, "Nauczyć się SQLAlchemy", False)`

Wtedy:

- `zadanie[0]` zwróci `1`
- `zadanie[1]` zwróci `"Nauczyć się SQLAlchemy"`
- `zadanie[2]` zwróci `False`

### SQLAlchemy ORM

W wersji ORM SQLAlchemy nie zwraca zwykłych krotek. Każdy rekord z tabeli `zadania` jest reprezentowany jako obiekt klasy `Zadanie` zdefiniowanej w pliku `models.py`.

Model `Zadanie` określa, jakie atrybuty posiada taki obiekt:

- `id` → identyfikator zadania
- `opis` → opis zadania
- `zrobione` → informacja, czy zadanie zostało wykonane

Dlatego zamiast korzystać z indeksów:

`zadanie[0]`, `zadanie[1]`, `zadanie[2]`

możemy odwoływać się bezpośrednio do atrybutów obiektu:

- `zadanie.id` → ID zadania
- `zadanie.opis` → opis zadania
- `zadanie.zrobione` → status zadania

Działa to dzięki mapowaniu ORM. Klasa `Zadanie` jest połączona z tabelą `zadania` przez:

`__tablename__ = "zadania"`

Natomiast `mapped_column()` definiuje kolumny tabeli jako atrybuty obiektu Pythona.

Przykładowo:

`id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)`

sprawia, że kolumna `id` z tabeli jest dostępna w Pythonie jako:

`zadanie.id`

### Najważniejsza różnica

**Raw SQL:** rekord jest krotką → korzystamy z `zadanie[0]`, `zadanie[1]`, `zadanie[2]`.

**SQLAlchemy ORM:** rekord jest reprezentowany przez obiekt `Zadanie` → korzystamy z `zadanie.id`, `zadanie.opis`, `zadanie.zrobione`.