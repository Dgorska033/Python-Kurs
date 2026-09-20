#  Zadanie 1 – Liczba produktów
# Napisz skrypt, który połączy się z bazą sklep.db i policzy, ile jest wszystkich produktów w
# tabeli Produkty. Użyj funkcji COUNT().

import sqlite3 

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT
COUNT(id_produktu) AS liczba_produktów
FROM Produkty
'''

c.execute(query)

wynik = c.fetchone()


print(f"Liczba wszystkich produktów: {wynik[0]}")

conn.close()
