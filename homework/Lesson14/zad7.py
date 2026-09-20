# Zadanie 7 – Zamówienia Anny Nowak
# Napisz skrypt, który wyświetli nazwy wszystkich produktów zamówionych przez klienta o
# imieniu 'Anna Nowak'. Będziesz potrzebować połączyć dane z czterech tabel: Klienci,
# Zamowienia, Zamowienia_Produkty i Produkty.

import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

imie_klienta = input("Podaj imię i nazwisko klienta: ")

c.execute('''--sql
    SELECT Produkty.nazwa_produktu
    FROM Produkty
    JOIN Zamowienia_Produkty
        ON Produkty.id_produktu = Zamowienia_Produkty.id_produktu
    JOIN Zamowienia
        ON Zamowienia_Produkty.id_zamowienia = Zamowienia.id_zamowienia
    JOIN Klienci
        ON Zamowienia.id_klienta = Klienci.id_klienta
    WHERE Klienci.imie = ?
''', (imie_klienta,))

wyniki = c.fetchall()

for wynik in wyniki:
    print(wynik[0])

conn.close()
