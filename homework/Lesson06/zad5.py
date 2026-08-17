# Zadanie 5 
#  Adnotacje i docstring: Weź funkcję kalkulator z zadania 1. Dodaj do niej pełne
# adnotacje typów dla wszystkich parametrów i wartości zwracanej. Napisz również
# kompletny docstring opisujący jej działanie

def kalkulator(a , b, operacja):
    """
    Oblicza proste działania matematyczne.
    
    Argumenty:
    a - przyjmowane jako int lub float bo przyjmuje oba typy
    b -  przyjmowane jako int lub float bo przyjmuje oba typy
    operacja - przyjmuje dany znak działania: +, -, * lub /

    Zwraca:
    wynik działania lub "Błąd" jeśli opercja została podana błędnie 

    """
    if operacja ==  "+": 
        return a + b 
    elif operacja == "-":
        return a - b 
    elif operacja == "*":
        return a * b
    elif operacja == "/":
        return a / b
    else: 
        return"Błąd"
   
print(type(kalkulator(10, 5, "+")))    # <class 'int'> 
print(type(kalkulator(2.5, 4.5, "+"))) # <class 'float'>
print(type(kalkulator(10, 5, "-")))    # <class 'int'>
print(type(kalkulator(10,5, "*")))     # <class 'int'>
print(type(kalkulator(10,5, "/")))     # <class 'float'>
print(type(kalkulator(10, 5,"%")))     # <class 'str'>