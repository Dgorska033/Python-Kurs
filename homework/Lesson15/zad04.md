Zadanie 4 – Dodanie priorytetu (Raw SQL)
Ręcznie zmodyfikuj tabelę zadania w database_raw.py (w funkcji init_db), dodając kolumnę
priorytet INTEGER DEFAULT 1. Następnie zaktualizuj funkcję dodaj_zadanie, aby
przyjmowała nowy argument i zapisywała go w bazie

## Dodanie priorytetu (Raw SQL)

Do tabeli `zadania` została dodana nowa kolumna:

`priorytet INTEGER DEFAULT 1`

Typ `INTEGER` oznacza, że priorytet przechowujemy jako liczbę całkowitą.

`DEFAULT 1` oznacza, że jeśli podczas tworzenia rekordu nie zostanie podana wartość priorytetu, baza może użyć domyślnej wartości `1`.

Funkcja `dodaj_zadanie()` została rozszerzona o nowy argument:

`priorytet: int`

Wcześniej funkcja przyjmowała tylko opis:

`dodaj_zadanie(opis)`

Po zmianie przyjmuje:

`dodaj_zadanie(opis, priorytet)`

Zapytanie `INSERT` również zostało rozszerzone o kolumnę `priorytet`.

Wcześniej zapisywane były:

`opis, zrobione`

Teraz zapisywane są:

`opis, zrobione, priorytet`

W `app_raw_sql.py` podczas dodawania zadania użytkownik podaje również jego priorytet, który następnie jest przekazywany do funkcji `dodaj_zadanie()`.

Ważne: `CREATE TABLE IF NOT EXISTS` tworzy tabelę tylko wtedy, gdy jeszcze nie istnieje. Nie aktualizuje struktury istniejącej tabeli. Dlatego zmiana definicji `CREATE TABLE` nie doda automatycznie kolumny `priorytet` do wcześniej utworzonej tabeli.