# Zadanie 5
# Logowanie błędów: Zmodyfikuj zadanie 1. tak, aby każdy napotkany wyjątek (wraz z jego
# treścią) był zapisywany do pliku log.txt , a program kontynuował działanie. Użyj bloku
# finally , aby upewnić się, że plik z logami jest zawsze zamykany.


def save_calculator(): 
    while True: 
        plik = None
        try: 
            plik = open("log.txt", "a")
            num1 = int(input("Provide first number: "))
            num2 = int(input("Provide second number: "))
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
                raise NameError
        except ValueError:  
            plik.write("Incorrect value") 
        except ZeroDivisionError: 
            plik.write("Can't devide by 0")  
        except NameError:
            plik.write("There is no such an operation")
        else: 
            print(f"The result: {wynik}") 
        finally:        
            kontynuacja = input("Would you like to continue: (yes/no): ").strip().lower()
            if kontynuacja == "no": 
                print("Thank you for using our calculator")     
            if plik: 
                plik.close()
    
save_calculator()

