# Zadanie 10 
#  Mini-projekt: Lista zadań: Stwórz prostą aplikację do zarządzania listą zadań. Program
# powinien:
# Przy starcie próbować wczytać zadania z pliku zadania.json .
# Pozwalać użytkownikowi dodać nowe zadanie.
# Pozwalać wyświetlić wszystkie zadania.
# Przy zamknięciu (lub na polecenie) zapisywać aktualną listę zadań do pliku
# zadania.json 

import json

# Próbujemy wczytać zadania zapisane podczas poprzedniego uruchomienia programu
try: 
    # "r" = read, czyli otwieramy plik tylko do odczytu
    with open("zadania.json", "r") as plik: 
        # json.load() odczytuje dane z pliku JSON
        # i zapisuje je do zmiennej "zadania" jako listę Pythona
        zadania = json.load(plik)


# Jeśli program uruchamiamy pierwszy raz i zadania.json jeszcze nie istnieje,
# zamiast błędu tworzymy pustą listę
except FileNotFoundError: 
    zadania = []


# Pobieramy od użytkownika jedno nowe zadanie
lista_zadan = input("Wpisz swoje zadanie na dzis: ")
# Dodajemy nowe zadanie na koniec listy "zadania"
zadania.append(lista_zadan)


# "w" = write, czyli otwieramy plik do zapisu
# Jeśli plik nie istnieje, Python go utworzy.
# Jeśli istnieje, jego zawartość zostanie zastąpiona aktualną listą.     
with open("zadania.json", "w", encoding="utf-8") as plik:
    # json.dump() zapisuje listę Pythona "zadania" do pliku JSON
    # indent=4 -> robi czytelne wcięcia w pliku
    # ensure_ascii=False -> poprawnie zapisuje polskie znaki
    json.dump(zadania, plik , indent=4, ensure_ascii=False) 
# Wyświetlamy aktualną listę zadań
print(f"Twoja lista zadań na dziś {zadania}")


# zadania = json.load(plik)
# json.dump(zadania, plik)