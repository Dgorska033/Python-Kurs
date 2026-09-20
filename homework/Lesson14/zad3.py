# Zadanie 3 – Suma wartości
# Oblicz i wyświetl łączną wartość wszystkich produktów z kategorii "Elektronika". Użyj funkcji
# SUM() oraz klauzuli WHERE z JOIN.


import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor() 

query = '''
SELECT 
SUM(p.cena) 
FROM Produkty as p
JOIN Kategorie AS k
    ON p.id_kategorii = k.id_kategorii
WHERE k.nazwa_kategorii = 'Elektronika'
'''

c.execute(query)

wynik = c.fetchone()


print(f"Wartość wszystkich produktów w kategorii 'Elektronika' {wynik[0]} zł")

conn.close() 