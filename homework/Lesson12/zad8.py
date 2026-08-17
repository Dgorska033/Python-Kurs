# Zadanie 8 – Kalkulator z pełną obsługą błędów
# Stwórz prosty kalkulator, który prosi użytkownika o podanie dwóch liczb i operacji (+, -, *, /).
# Całość umieść w pętli while True , aby program działał do momentu przerwania.
# Użyj bloku try...except do obsługi:
# ValueError , jeśli użytkownik wpisze coś, co nie jest liczbą.
# ZeroDivisionError przy próbie dzielenia przez zero.
# Użyj bloku else , aby wyświetlić wynik tylko wtedy, gdy nie było błędu.
# Użyj bloku finally , aby na koniec każdej iteracji pętli wyświetlić komunikat "Koniec
# obliczeń.".


def calculator(): 
    while True: 
        try: 
            num1 = float(input("Provide first number: "))
            num2 = float(input("Provide second number: "))
            operation = input("Provide operation on numbers e.g.(+, -, *, /): ")
            if operation == "+":
                wynik = num1 + num2
            elif operation == "-":
                wynik = num1 - num2
            elif operation == "*":
                wynik = num1 * num2
            elif operation == "/": 
                wynik = num1 / num2  
            else: 
                print("There is no such an operation")
                continue
        except ValueError:  
            print("Incorrect value") 
        except ZeroDivisionError: 
            print("Can't devide by 0")  
        except NameError:
            print("There is no such an operation")
        else: 
            print(f"The result: {wynik}") 
        finally: 
                print("End of the calculation block") 
                break 
calculator() 

