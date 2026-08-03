# Zadanie 4
# Odczyt konfiguracji: Napisz program, który odczytuje plik config.json z poprzedniego
# zadania i wyświetla komunikat: Witaj, [uzytkownik]! Twój motyw to [motyw].

import json

# konfiguracja = {
#   "uzytkownik": "admin", 
#   "motyw": "ciemny", 
#   "rozdzielczosc": [1920, 1080]
# }

with open("konfiguracja.json", "r", encoding="utf-8") as plik: # r - do odczytu 
                      
    dane = json.load(plik)       #indent=4 dodaje wcięcia, dzięki czemu plik jest czytelny
                                # ensure_ascii=False zapisuje polskie znaki (ą, ć, ę...) zamiast kodów Unicode
    print(f"Witaj, {dane["uzytkownik"]}! Twój motyw to {dane["motyw"]}.")

