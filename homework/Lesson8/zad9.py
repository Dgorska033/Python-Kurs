# Zadanie 9: 
# Kontekstowy menedżer with : Pokaż, jak instrukcja with open(...) as f: upraszcza
# kod z zadania 3, eliminując potrzebę jawnego używania bloku finally do zamykania
# pliku

plik = None 

def moje_pliki():
    try:   
        with open("moj_pliki.pdf", "r") as f:
            print(f.read("moj_pliki.pdf"))
    except FileNotFoundError:
        print("Plik nie istnieje")
    except PermissionError:   # jeśli nie byłoby uprawnień a plik by istniał to by przeszło tutaj, narazie zatrzymuje sie na file not found 
        print("Brak uprawnień") 

moje_pliki()

# with open - martwi się za nas, i sam zamyka plik - my nie musimy tego robić w finally