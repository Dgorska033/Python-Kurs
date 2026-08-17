# # Zadanie 1 - Kalkulator:
#  Napisz funkcję kalkulator(a, b, operacja) , która przyjmuje dwie liczby i
# string z operacją ( "+" , "-" , "*" lub / "). Funkcja powinna zwracać wynik
# odpowiedniego działania

def kalkulator(a, b, operacja):
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
   
print(kalkulator(10, 5, "+"))
print(kalkulator(2.5, 4.5, "+"))
print(kalkulator(10, 5, "-"))
print(kalkulator(10,5, "*"))
print(kalkulator(10,5, "/"))
print(kalkulator(10, 5,"%"))