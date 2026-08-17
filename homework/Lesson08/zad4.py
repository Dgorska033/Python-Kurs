# Zadanie 4
#  Asercja w funkcji: Stwórz funkcję oblicz_srednia(lista_ocen) , która zwraca średnią z
# listy. Użyj assert , aby upewnić się, że przekazana lista nie jest pusta

def stworz_srednia(*lista_ocen):
    assert len(lista_ocen) > 0, "Lista jest pusta"  # assert warunek, "Komunikat"

    return sum(lista_ocen) / len(lista_ocen)

print(f"{stworz_srednia(3,5,5):.2f}")
print(f"{stworz_srednia(6,6,6,1):.2f}")
print(stworz_srednia())

