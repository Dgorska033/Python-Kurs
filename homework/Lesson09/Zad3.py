# Zadanie 3 
#  Konfiguracja w JSON: Stwórz słownik Pythona z ustawieniami aplikacji, np.
# konfiguracja = {"uzytkownik": "admin", "motyw": "ciemny", "rozdzielczosc":
# [1920, 1080]} . Zapisz ten słownik do pliku config.json z wcięciami i poprawnym
# kodowaniem polskich znaków

import json
# Słownik z ustawieniami aplikacji
konfiguracja = {
  "uzytkownik": "admin", 
  "motyw": "ciemny", 
  "rozdzielczosc": [1920, 1080]
  } 
                        # Otwórz (lub utwórz) plik konfiguracja.json do zapisu
                        # encoding="utf-8" pozwala poprawnie zapisać polskie znaki
with open("konfiguracja.json", "w", encoding="utf-8") as plik:
                        # Zapisz słownik do pliku w formacie JSON
                        # indent=4 dodaje wcięcia, dzięki czemu plik jest czytelny
                        # ensure_ascii=False zapisuje polskie znaki (ą, ć, ę...) zamiast kodów Unicode
    json.dump(konfiguracja, plik, indent=4,  ensure_ascii=False)



# .dump() -> wyrzucić, zrzucić, wyeksportować dane.
"""
dump() → zapisuje do pliku. dump = zapisz dane do jakiegoś formatu
dumps() → tworzy JSON jako string.

.write() do zapisyawanie zwyklego tesktu 
.dump()  do zapisywania całych struktur danych Pythona (np. słowników, list) jako JSON.
"""

