# Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
# try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
# użytkownikow

plik = None

try: 
    with open("nieistniejacy.txt", "r",  encoding="utf-8") as plik:
        plik.load()
except FileNotFoundError:
    print("Błąd: Nie znaleziono pliku")

    
