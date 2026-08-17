#  Zadanie 2 – Atrybuty Produkt
# Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz
# obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.

class Produkt: 
    def __init__(self, nazwa, cena, kategoria): # __init__ ma dokładnie dwa podkreślniki, usuchamia się automatycznie podczas tworzenia obiektu
        # np. self.nazwa to to atrybut konkretnego obiektu
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria
"""Bez return __init__  tylko "wypełnia" obiekt danymi. Python sam tworzy obiekt, a __init__ przypisuje
mu np. nazwe cene i kategorie"""


# tworzę jeden produkt i od razu przekazuję wszystkie dane w takiej kolejnosci, w jakiej ustalilam w __init__
produkt1 = Produkt("Samsung Galaxy", 1700, "telefon")

# Atrybuty odczytuję przez: nazwa_obiektu.nazwa_atrybutu, bez (), bo atrybuty nie są funkcją/ metodą
print(produkt1.nazwa)
print(produkt1.cena)
print(produkt1.kategoria)


