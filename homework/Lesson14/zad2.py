#  Zadanie 2 – Najdroższy produkt
# Napisz skrypt, który znajdzie nazwę i cenę najdroższego produktu w sklepie. Użyj funkcji
# MAX().

import sqlite3 

conn = sqlite3.connect('sklep.db')
c = conn.cursor() 

query = '''
SELECT 
MAX(cena) as najwyzsza_cena
FROM Produkty
'''

c.execute(query)

wynik = c.fetchone() 


print(f"Cena najdroższego produktu: {wynik[0]}")

conn.close()
