# Zadanie 7 
# Zwracanie wielu wartości: Stwórz funkcję analiza_listy(lista: list[int]) , która
# przyjmuje listę liczb i zwraca krotkę zawierającą trzy wartości: minimum, maksimum i sumę
# elementów z listy.

def analiza_listy(lista: list[int]): 
    
    minimum = min(lista)
    maksimum = max(lista) 
    suma = sum(lista)
    return minimum, maksimum, suma
   

print(analiza_listy([10,5,4,27,8]))
