# Zadanie 6
#  Przerzucanie wyjątku: Napisz funkcję przetworz_dane(dane) , która w bloku
# try...except łapie KeyError (np. przy próbie dostępu do nieistniejącego klucza w
# słowniku), loguje go, a następnie rzuca ( raise ) nowy, własny wyjątek


# Tworzę własny wyjątek, z którego będę korzystać
class BladPrzetwarzaniaDanych(Exception):
    pass

def przetworz_dane(dane): 
    try: 
        # Pobiera dane ze słownika
        imie = dane["imie"]
        wiek = dane["wiek"]
        miasto = dane["miasto"]
    except KeyError as e:
         # Loguję informację o brakującym kluczu
        print(f"Brakuje danych {e}") # logowanie
         # Rzucam własny wyjątek zamiast KeyError
        raise BladPrzetwarzaniaDanych from e
    else: 
        # Ten blok wykona się tylko wtedy,
        # gdy w try nie wystąpi żaden wyjątek
        print(f"Hej jesteś {imie}, masz lat {wiek} i pochodzisz z {miasto}")


# Poprawny słownik
dane = {
    "imie": "Dominika",
    "wiek": 23,
    "miasto": "Warszawa"
}

# Słownik z brakującym kluczem "miasto"
brakujace_dane = {
    "imie": "Dominika",
    "wiek": 23
}

try:
     # Wywołuje funkcję
    przetworz_dane(dane)
    przetworz_dane(brakujace_dane)
except BladPrzetwarzaniaDanych: 
# Łapię własny wyjątek
    print() 
