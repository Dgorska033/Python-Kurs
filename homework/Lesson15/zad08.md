Zadanie 8 – Refaktoryzacja do klas (Raw SQL)
Przepisz aplikację app_raw_sql.py i database_raw.py używając klas. Stwórz klasę
TaskManagerRaw, która w konstruktorze inicjalizuje bazę, a jej metody (dodaj, pobierz itd.)
wykonują operacje na bazie.

Refaktoryzacja do klas (Raw SQL)

Aplikacja Raw SQL została przepisana z funkcji na klasę `TaskManagerRaw`.

Klasa `TaskManagerRaw` odpowiada za wykonywanie operacji na bazie danych SQLite.

W konstruktorze `__init__()` zapisywana jest nazwa bazy danych:

`self.database_name = database_name`

oraz automatycznie wywoływana jest metoda:

`self.init_db()`

Dzięki temu baza danych jest inicjalizowana podczas tworzenia obiektu klasy.

Dotychczasowe funkcje zostały przekształcone w metody klasy:

- `init_db()` – inicjalizuje bazę danych i tworzy tabelę
- `dodaj_zadanie()` – dodaje nowe zadanie
- `pobierz_zadania()` – pobiera zadania z bazy
- `oznacz_jako_zrobione()` – zmienia status zadania
- `usun_zadanie()` – usuwa zadanie
- `wyszukaj_zadania()` – wyszukuje zadania po fragmencie opisu

W `app_raw_sql.py` klasa jest importowana:

`from database_raw import TaskManagerRaw`

Następnie tworzony jest jej obiekt:

`manager = TaskManagerRaw()`

Operacje na bazie nie są już wykonywane przez:

`db.dodaj_zadanie()`

tylko przez metody utworzonego obiektu:

`manager.dodaj_zadanie()`

Analogicznie pozostałe operacje wykonywane są przez:

`manager.pobierz_zadania()`

`manager.oznacz_jako_zrobione()`

`manager.usun_zadanie()`

`manager.wyszukaj_zadania()`

Funkcja `pokaz_zadania()` otrzymuje obiekt `manager` jako argument, dzięki czemu również może korzystać z metod klasy `TaskManagerRaw`.

Najważniejsza różnica:

wcześniej logika bazy danych była zbiorem oddzielnych funkcji w module, natomiast po refaktoryzacji została zgrupowana wewnątrz jednej klasy odpowiedzialnej za zarządzanie zadaniami.