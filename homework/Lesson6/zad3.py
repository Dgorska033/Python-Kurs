# # Zadanie 3 - 
# Średnia ocen: Napisz funkcję oblicz_srednia(*args) , która przyjmuje dowolną liczbę
# ocen (argumentów pozycyjnych) i zwraca ich średnią arytmetyczną. Jeśli nie podano żadnej
# oceny, powinna zwrócić 0.


def oblicz_srednia(*oceny):   # Funkcja może przyjąć tyle ocen, ile podam

    if not oceny:
        return 0 # jeśli nie podano żadnej oceny, zwróć 0

    return sum(oceny) / len(oceny)     
 # sum() dodaje wszystkie oceny
 # len() liczy, ile ich jest
print(oblicz_srednia(4,5,1))
print(oblicz_srednia())
