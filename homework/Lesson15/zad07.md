Zadanie 7 – Wyszukiwanie po opisie (SQLAlchemy)
Zaimplementuj tę samą funkcjonalność w aplikacji ORM. Użyj metody .filter() oraz metody
.contains() na kolumnie, np. db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all().

Raw SQL                         SQLAlchemy ORM

SELECT * FROM zadania          db.query(Zadanie)
WHERE opis LIKE '%fraza%'  >   .filter(Zadanie.opis.contains(fraza))
fetchall()                  >   .all()


 Wyszukiwanie po opisie (SQLAlchemy ORM)

W tym zadaniu została dodana możliwość wyszukiwania zadań po fragmencie ich opisu w wersji SQLAlchemy ORM.

W pliku `database.py` została utworzona funkcja `wyszukaj_zadania(fraza)`.

Do wyszukiwania wykorzystane zostało zapytanie:

db.query(Zadanie).filter(Zadanie.opis.contains(fraza)).all()

Poszczególne elementy oznaczają:

db.query(Zadanie)
-> wybiera obiekty klasy `Zadanie` z bazy danych

.filter(...)
-> nakłada warunek na wyszukiwane zadania

Zadanie.opis.contains(fraza)
-> sprawdza, czy kolumna `opis` zawiera podaną przez użytkownika frazę

.all()
-> pobiera wszystkie zadania spełniające warunek

`contains()` w SQLAlchemy pełni tutaj podobną funkcję jak użyte wcześniej w Raw SQL:

WHERE opis LIKE '%fraza%'

W pliku `app_orm.py` została dodana opcja „Wyszukaj zadanie”.

Program:

1. Pobiera od użytkownika szukaną frazę.
2. Przekazuje ją do funkcji `db.wyszukaj_zadania(fraza)`.
3. Sprawdza, czy zostały znalezione pasujące zadania.
4. Za pomocą pętli `for` wyświetla wszystkie znalezione zadania.
5. Jeśli nie znaleziono żadnego zadania, wyświetla odpowiedni komunikat.

Ważna różnica między Raw SQL a SQLAlchemy ORM:

W Raw SQL wyniki były zwracane jako krotki, dlatego korzystaliśmy z indeksów:

zadanie[0] -> ID  
zadanie[1] -> opis  
zadanie[2] -> status

W SQLAlchemy wyniki są obiektami klasy `Zadanie`, dlatego możemy korzystać bezpośrednio z ich atrybutów:

zadanie.id -> ID  
zadanie.opis -> opis  
zadanie.zrobione -> status

Dzięki ORM nie musimy pamiętać, pod którym indeksem znajduje się konkretna wartość. Korzystamy z nazw atrybutów zdefiniowanych w modelu `Zadanie`.