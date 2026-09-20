# Zadanie 8 – Kategorie z liczbą produktów
# Napisz zapytanie, które wyświetli nazwę każdej kategorii oraz liczbę produktów należących
# do tej kategorii. Użyj JOIN, COUNT() oraz GROUP BY.

import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor() 

c.execute('''--sql 
    SELECT COUNT(*), k.nazwa_kategorii
    FROM Kategorie k 
    JOIN Produkty p 
        ON p.id_kategorii = k.id_kategorii
    GROUP BY k.nazwa_kategorii
''')

kategoria_ilosc = c.fetchall() 

print("Ilość produktów w danej kategorii:") 
for ilosc, nazwa in kategoria_ilosc:
    print(f"{nazwa}, {ilosc}")


conn.close() 

