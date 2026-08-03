# Zadanie 3 
# Czytanie pliku: Napisz funkcję, która próbuje otworzyć i odczytać plik o podanej nazwie.
# Obsłuż wyjątki FileNotFoundError (gdy pliku nie ma) oraz PermissionError (gdy nie
# ma uprawnień do odczytu).


def moje_pliki():
    plik = None
    try:    
        plik = open("moj_pliki.pdf", "r") # r = czytaj plik
        zawartosc = plik.read()  # czyta całą jego zawartość.
        print(zawartosc)  # wyświetla zawarośc
    except FileNotFoundError:
        print("Plik nie istnieje")
    except PermissionError:   # jeśli nie byłoby uprawnień a plik by istniał to by przeszło tutaj, narazie zatrzymuje sie na file not found 
        print("Brak uprawnień") 
    finally: 
        if plik:
            plik.close()

moje_pliki()

