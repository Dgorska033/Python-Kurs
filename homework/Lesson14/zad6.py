# Zadanie 6 – Produkty droższe od średniej
# Napisz skrypt, który wyświetli nazwy i ceny wszystkich produktów, których cena jest wyższa
# niż średnia cena wszystkich produktów w sklepie. Wykorzystaj podzapytanie

import sqlite3
conn = sqlite3.connect('sklep.db')
c = conn.cursor()

c.execute('''--sql
    SELECT AVG(cena) FROM Produkty
''')

srednia_cena = c.fetchone()
print(f"Produkty droższe niż średnia cena ({srednia_cena[0]:.2f}) zł")

query = '''--sql 
    SELECT nazwa_produktu, cena 
    FROM Produkty
    WHERE cena > (SELECT AVG(cena) FROM Produkty)
'''
c.execute(query)
wyniki = c.fetchall()

for wynik in wyniki:
    print(f"-{wynik[0]}: {wynik[1]:.2f} zł")

conn.commit()
conn.close()

