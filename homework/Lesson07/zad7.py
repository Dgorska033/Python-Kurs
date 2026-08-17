# Zadanie 7 
# Dekorator logujący: Napisz dekorator @loguj , który przed wywołaniem udekorowanej
# funkcji wypisze komunikat Uruchamiam funkcję [nazwa_funkcji]... , a po jej
# zakończeniu Zakończono funkcję [nazwa_funkcji]. .

def loguj(func): 
#   Dekorator wyświetlający nazwę funkcji przed i po wywołaniu funkcji
    def wrapper(*args, **kwargs):  # To uruchamia się zamiast naszej funkcji wyzej.
        print(f"Uruchamiam funkcję {func.__name__}")  # informacja, że funkcja zaraz wystartuje.
        nazwa = func(*args, **kwargs)  # uruchamia funkcje i zapmietuje co zwroci
        print(f"Zakończono funkcję {func.__name__}")  # drugi komunikat
        return nazwa  # Oddaj wynik funkcji dalej.
    return wrapper    # Zwróć wrapper zamiast naszej funkcji.

@loguj
def funny(powtorz:str , ilosc: int) -> None: #  # Zwykła funkcja wypisująca tekst kilka razy.
    print(f"{powtorz}" * ilosc )

funny(" Powtórz ", 5)


