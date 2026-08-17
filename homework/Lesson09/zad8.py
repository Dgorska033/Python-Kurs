# Zadanie 8 
#  Wyszukiwarka logów: Wyobraź sobie, że masz duży plik log.txt . Napisz program, który
# pyta użytkownika o szukane słowo (np. "ERROR") i zapisuje wszystkie linie zawierające to
# słowo do nowego pliku wyniki_wyszukiwania.txt

from pathlib import Path 

wyszukiwanie = input("Podaj słowo którego szukasz: ") 

try: 
    folder = Path(__file__).parent
    sciezka = folder / "tekst.txt"
    with open(sciezka, "r", encoding="utf-8") as plik:
        with open("wyniki_wyszukiwania.txt", "w", encoding="utf-8") as plik_wynikowy:
            znaleziono = False 
            for linia in plik: 
                if wyszukiwanie in linia: 
                    plik_wynikowy.write(linia)
                    znaleziono = True 
            if not znaleziono:
                raise ValueError
        print("Wyniki pomyślne zapisane w pliku")
except ValueError:
    print("Wystąpił błąd: szukany tekst nie istnieje w pliku!")

          