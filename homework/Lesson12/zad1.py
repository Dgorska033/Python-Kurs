# Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je

from dataclasses import dataclass

@dataclass
class Film:
    tytuł : str 
    reżyser : str
    rok_produkcji : int

film1 = Film("Batman", "Ktoś tam", 2003)
film2 = Film("Titanic", "Słabo się znam na filmach", 1999)

print(film1)
print(film2)
