# Zadanie 6
#  Licznik wywołań: Stwórz domknięcie (closure). Napisz funkcję stworz_licznik() , która
# zwraca funkcję. Każde wywołanie zwróconej funkcji powinno zwiększać wewnętrzny licznik i
# zwracać jego aktualną wartość.

def stworz_licznik(number):  # funkcja nadrzędna 
    def licznik():  # clousure - funkcja zagnieżdżona
        nonlocal number  # (number) odowłanie do zmiennej z zakresu funkcji nadrzędnej, klucz > nonlocal pozwala modyfikować zmienne 
        # z zewnętrznego zakresu a nie tylko jego odczyt 
        number += 1   # polecenie zwiększamy o 1 
        return number 
    return licznik 

liczenie = stworz_licznik(0) 

print(liczenie())
print(liczenie())
print(liczenie())

