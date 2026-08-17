# Zadanie 4 – Bezpieczne dzielenie
# Napisz funkcję bezpieczne_dzielenie(a, b), która zwraca wynik dzielenia a / b. Użyj bloku
# try...except, aby obsłużyć błąd ZeroDivisionError. Jeśli wystąpi ten błąd, funkcja powinna
# zwrócić None i wyświetlić komunikat "Błąd: Dzielenie przez zero!".

def bezpieczne_dzielnie(a, b):
    try: 
        return  a / b
    except ZeroDivisionError:
        print("Bład nie można dzielić przez 0")

print(f" Wynik dzielenia to : {bezpieczne_dzielnie(10, 5)}")
print(f" Wynik dzielenia to : {bezpieczne_dzielnie(10, 0)}") # Bład nie można dzielić przez 0
 #  Wynik dzielenia to : None

