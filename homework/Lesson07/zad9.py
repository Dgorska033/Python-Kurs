# Zadanie 9 
# Dekorator z argumentem: Stwórz dekorator @powtorz(n) , który przyjmuje argument n i
# powoduje, że udekorowana funkcja zostanie wykonana n razy.

def powtorz(n):  # n mówi, ile razy ma zostać wykonana funkcja.
    def dekorator(func):  # Dekorator dostaje funkcję, którą chcemy powtórzyć.
        def wrapper(*args, **kwargs):  # Tutaj wykonamy funkcję kilka razy.
            wynik = None  # Tu zapiszemy wynik ostatniego wywołania funkcji.

            # Powtarzaj funkcję tyle razy, ile podano w n.
            for i in range(n): 
                wynik = func(*args, **kwargs)
            return wynik    # Zwróć wynik ostatniego wywołania funkcji.
        return wrapper      # Oddaj wrapper zamiast oryginalnej funkcji.
    return dekorator        # Zwróć dekorator z zapamiętaną wartością n.

@powtorz(5)                  # Powtórz funkcję 5 razy.
def powitanie():
    print("Siemańsko") 
powitanie() 

       
