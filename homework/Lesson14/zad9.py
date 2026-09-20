# Zadanie 9 – Funkcja do wyszukiwania produktów
# Napisz w Pythonie funkcję znajdz_produkty_w_kategorii(nazwa_kategorii), która przyjmuje
# jako argument nazwę kategorii i zwraca listę krotek (nazwa_produktu, cena) dla wszystkich
# produktów w tej kategorii.

import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor() 

znajdz = input("Podaj nazwę kategorii: ")


def znajdz_produkty_w_kategorii(nazwa_kategorii):
    c.execute('''--sql 
        SELECT nazwa_produktu, cena 
        FROM Produkty
        JOIN Kategorie ON Produkty.id_kategorii = Kategorie.id_kategorii
        WHERE Kategorie.nazwa_kategorii = ? 
    ''', (nazwa_kategorii,))

    wynik = c.fetchall()

    return wynik

produkty = znajdz_produkty_w_kategorii(znajdz)

print(produkty)

conn.close()

