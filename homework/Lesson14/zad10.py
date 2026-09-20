# Zadanie 10 – Prosta symulacja ORM
# Stwórz klasę Produkt w Pythonie z atrybutami id_produktu, nazwa_produktu i cena.
# Następnie napisz funkcję pobierz_wszystkie_produkty(), która połączy się z bazą danych,
# pobierze wszystkie produkty i zwróci listę obiektów klasy Produkt. To ćwiczenie pokaże Ci,
# jak ORM automatyzuje mapowanie wierszy na obiekty.

import sqlite3

class Produkt():
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena


def pobierz_wszytskie_produkty():
    conn = sqlite3.connect('sklep.db')
    c = conn.cursor()

    c.execute('''SELECT id_produktu, nazwa_produktu, cena FROM Produkty''')

    lista_produktow = c.fetchall()  

    produkty = [
        Produkt(id_produktu, nazwa, cena)
        for id_produktu, nazwa, cena in lista_produktow
    ]

    conn.close() 
    return produkty

pobrane = pobierz_wszytskie_produkty()
print("POBRANE PRODUKTY:")

for p in pobrane:
    print(f"{p.id_produktu} {p.nazwa_produktu} {p.cena}")

    
    