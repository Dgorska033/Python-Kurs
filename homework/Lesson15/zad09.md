Zadanie 9 – Dodanie tagów do zadań (SQLAlchemy)
Rozbuduj aplikację ORM o system tagów. Będziesz potrzebować:
a. Nowego modelu Tag (id, nazwa).
b. Tabeli pośredniej do obsługi relacji wiele-do-wielu między zadaniami a tagami.
c. Zdefiniowania relacji relationship w modelach Zadanie i Tag.
d. Wygenerowania i zastosowania migracji.
e. Zmodyfikowania logiki aplikacji, aby można było dodać taga do zadania.

# Zadanie 9 – Dodanie tagów do zadań (SQLAlchemy)

W tym zadaniu aplikacja ORM została rozbudowana o system tagów.

Tag jest etykietą przypisaną do zadania, np. `python`, `szkoła`, `pilne` lub `zakupy`.

## Model Tag

W `models.py` został utworzony nowy model `Tag`.

Model posiada:

`id` -> unikalne ID taga

`nazwa` -> nazwę taga

Dzięki temu tagi są przechowywane w osobnej tabeli `tagi`.


## Relacja wiele-do-wielu

Jedno zadanie może posiadać wiele tagów, a jeden tag może być przypisany do wielu zadań.

Przykład:

Zadanie „Nauczyć się SQLAlchemy” może mieć tagi:

- `python`
- `nauka`
- `pilne`

Jednocześnie tag `python` może być przypisany również do innych zadań.

Jest to relacja wiele-do-wielu (many-to-many).


## Tabela pośrednia

Do połączenia zadań z tagami została utworzona tabela:

`zadania_tagi`

Przechowuje ona dwa klucze obce:

`zadanie_id` -> wskazuje zadanie

`tag_id` -> wskazuje tag

Przykładowy wpis:

zadanie_id = 1  
tag_id = 2

oznacza, że zadanie o ID 1 posiada tag o ID 2.


## Relationship

W modelu `Zadanie` została zdefiniowana relacja:

`tagi`

Dzięki temu można odwoływać się do tagów konkretnego zadania przez:

`zadanie.tagi`

W modelu `Tag` została utworzona relacja odwrotna:

`zadania`

Dzięki temu można sprawdzić, do których zadań przypisany jest konkretny tag.

`back_populates` łączy obie strony tej samej relacji.


## Migracja Alembic

Po zmianie modeli została wygenerowana nowa migracja:

`.\.venv\Scripts\python.exe -m alembic revision --autogenerate -m "dodanie tagow"`

Alembic poprawnie wykrył dwie nowe tabele:

`tagi`

`zadania_tagi`

Następnie migracja została zastosowana za pomocą:

`.\.venv\Scripts\python.exe -m alembic upgrade head`

Po migracji baza ORM zawiera między innymi:

- `zadania`
- `tagi`
- `zadania_tagi`
- `alembic_version`


## Dodawanie taga do zadania

W `database.py` została dodana funkcja `dodaj_tag_do_zadania()`.

Funkcja:

1. Wyszukuje zadanie po jego ID.
2. Sprawdza, czy tag o podanej nazwie już istnieje.
3. Jeśli tag nie istnieje, tworzy nowy obiekt `Tag`.
4. Dodaje tag do listy `zadanie.tagi`.
5. Zapisuje zmiany za pomocą `db.commit()`.

Przed dodaniem taga sprawdzane jest również:

`if tag not in zadanie.tagi`

Dzięki temu ten sam tag nie jest przypisywany wielokrotnie do tego samego zadania.


## Najważniejsze

Relacja wiele-do-wielu wymaga trzech elementów:

`Zadanie` <-> `zadania_tagi` <-> `Tag`

Tabela `zadania_tagi` jest łącznikiem pomiędzy zadaniami i tagami.

SQLAlchemy pozwala później pracować z tą relacją za pomocą obiektów:

`zadanie.tagi.append(tag)`

bez konieczności ręcznego dodawania rekordów do tabeli pośredniej.