#  Zadanie 4 – Średnia cena książki
# Napisz zapytanie, które obliczy średnią cenę produktów w kategorii "Książki". Użyj AVG().
 
import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor() 

query = '''
SELECT
AVG(p.cena) 
FROM Produkty as p
JOIN Kategorie AS k
    ON p.id_kategorii = k.id_kategorii
WHERE k.nazwa_kategorii = ?;
'''

c.execute(query, ("Książki",))

wynik = c.fetchone()

# fetchone() zwraca krotkę, np. (39.99,)
# [0] wyciąga z niej pierwszą wartość, czyli wynik AVG()
srednia_cena = wynik[0]
print(f"Średnia cena produktu w kategorii 'Książki' to:  {srednia_cena:.2f} zł")

conn.close() 

