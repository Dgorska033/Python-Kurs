# Zadanie 9 - Prosty kalkulator 

num1 = float(input("Podaj pierwszą liczbę: \n")) 
num2 = float(input("Podaj drugą liczbę: \n")) 

operator = input("Podaj działanie (+, -, *, /):") 

if operator == "+": 
    print(f"Wynik: {num1 + num2}")
elif operator == "-": 
    print(f"Wynik: {num1 - num2}") 
elif operator == "*": 
    print(f"Wynik: {num1 * num2}")
elif operator == "/": 
    if num2 !=0:
        print(f"Wynik: {num1 / num2}") 

    else: 
        print("Błąd: NIE MOŻNA DZIELIĆ PRZEZ 0") 
else: 

    print("Niepraidłowy operator") 