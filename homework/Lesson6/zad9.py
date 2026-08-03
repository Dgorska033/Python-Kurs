# Zadanie 9 -
# Silnia (rekurencja): Napisz funkcję silnia(n: int) -> int , która oblicza silnię liczby n
# w sposób rekurencyjny (czyli wywołując samą siebie). Pamiętaj o warunku bazowym: silnia
# z 0 to 1. (Wzór: n! = n * (n-1)! )

def silnia(n:int) -> int:
    if n == 0: 
       return 1 
    else:
        return n * silnia(n-1)
print(silnia(0)) 
print(silnia(1)) 
print(silnia(2)) 
print(silnia(3)) 
print(silnia(4)) 
print(silnia(5)) 

# silnia to działanie: jesli widzimy liczby to znaczy że przez wszystkie kolejne liczby naturalne aż do 1. 
# dla 5 to np: 5! = 5X4x3x2x1
# 0! to zawsze 1 dla 1! to też 1
# python nie rozumie 1! - silnia w taki sposób, więc trzeba mu rozpisać wzór. =! - oznacza wtedy rozne od więc też nie zadziała