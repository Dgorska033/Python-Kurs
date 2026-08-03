# Zadanie 10 -  Komentowanie kodu:

def oblicz_pole_prostokata(a, b):
    """
     Def definiuje funckje, używamy tego aby nie pisać kilka razy tego samego kodu.
     Wymaga to zmiennej ktorą jest a i b.
     Zapakowywanie kawałka kodu aby użyć go pózniej.
    """
    
    pole = a * b # W tej linii, przekazujemy Pythonowi zadanie do wykonania 
    return pole  # Używamy instukcji return aby zwrócić wartość do miejca w którym funkcja została wywołana 
bok_a = 10
bok_b = 20
wynik = oblicz_pole_prostokata(bok_a, bok_b)
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")

