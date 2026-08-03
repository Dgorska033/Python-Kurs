# Zadanie 8 

# Bezpieczny kalkulator: Napisz program, który w pętli prosi użytkownika o podanie dwóch
# liczb i operacji ( + , - , * , / ). Zaimplementuj pełną obsługę błędów ValueError (gdy
# dane nie są liczbami) i ZeroDivisionError . Dodaj blok else do wyświetlania wyniku i
# finally z komunikatem "Kolejna operacja..."


def save_calculator(): 
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
            kontynuacja = input("Would you like to continue: (yes/no): ").strip().lower()
            if kontynuacja == "no": 
                print("Thank you for using our calculator") 
                break 
save_calculator() 



