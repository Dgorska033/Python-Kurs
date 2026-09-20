Zadanie 6 – Wyszukiwanie po opisie (Raw SQL)
Dodaj do aplikacji app_raw_sql.py funkcję wyszukiwania zadań. Użytkownik podaje frazę, a
program wyświetla wszystkie zadania, których opis zawiera tę frazę. Użyj operatora LIKE i
wzorca %fraza% w zapytaniu SELECT.

Wyszukiwanie po opisie (Raw SQL)

W tym zadaniu została dodana możliwość wyszukiwania zadań po fragmencie ich opisu.

W pliku `database_raw.py` została utworzona funkcja `wyszukaj_zadania(fraza)`, która pobiera od użytkownika szukaną frazę i wykonuje zapytanie SQL:

SELECT * FROM zadania WHERE opis LIKE ?

Do wyszukiwanej frazy dodawane są znaki `%`:

wzorzec = f"%{fraza}%"

Znak `%` w operatorze `LIKE` oznacza dowolny ciąg znaków.

Dzięki temu wpisanie np. `zakup` może znaleźć zarówno:

- `Zrobić zakupy`
- `Zakupy na weekend`
- `Lista zakupów`

Funkcja `fetchall()` zwraca wszystkie rekordy pasujące do wyszukiwanej frazy.

W pliku `app_raw_sql.py` została dodana nowa opcja menu „Wyszukaj zadanie”.

Program:

1. Pobiera frazę od użytkownika.
2. Przekazuje ją do funkcji `db.wyszukaj_zadania(fraza)`.
3. Sprawdza, czy znaleziono jakieś zadania.
4. Za pomocą pętli `for` wyświetla wszystkie znalezione rekordy wraz z ID, opisem, statusem i priorytetem.
5. Jeśli lista wyników jest pusta, wyświetla informację, że nie znaleziono pasujących zadań.

W Raw SQL każdy rekord zwracany przez `fetchall()` jest krotką:

zadanie[0] -> ID  
zadanie[1] -> opis  
zadanie[2] -> status zrobione  
zadanie[3] -> priorytet

Ważne:

`else` informujący o braku wyników należy do `if wyniki`, a nie do pętli `for`.

Python pozwala na konstrukcję `for ... else`, dlatego nieprawidłowe wcięcie powodowało wcześniej, że komunikat „Nie znaleziono zadań” pojawiał się nawet po znalezieniu i wyświetleniu zadania.
