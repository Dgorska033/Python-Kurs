# Zadanie 6
# Import z CSV: Napisz program, który odczytuje plik produkty.csv i oblicza sumę cen
# wszystkich produktów. Użyj csv.DictReader , aby łatwiej odwoływać się do kolumn po
# nazwach

from pathlib import Path 
import csv 

sciezka = Path(__file__).parent.parent.parent / "produkty.csv" 

with open(sciezka, "r", encoding="utf-8") as f: 
    reader = csv.DictReader(f, delimiter=';') # "delimiter" must be a 1-character string
    suma = 0

    for wiersz in reader: 
        suma = float(wiersz["cena"]) + suma # Sumujemy wartości z kolumny cena
    print(f"Suma wartości z pliku wynosi: {suma}") 


