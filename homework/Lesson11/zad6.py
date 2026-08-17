# Zadanie 6 – Wektor 2D i przeciążanie operatorów
# Stwórz klasę Wektor2D z atrybutami x i y. Przeciąż następujące operatory:
# __add__(self, other) : do dodawania dwóch wektorów (dodajemy odpowiadające
# sobie współrzędne).
# __sub__(self, other) : do odejmowania wektorów.
# eq(self, other): do porównywania, czy dwa wektory są równe (mają te same x i y).
# Dodatkowo zaimplementuj str do ładnego wyświetlania. Przetestuj działanie, tworząc
# dwa wektory i wykonując na nich wszystkie zaimplementowane operacje.

class Wektor2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# (+) __add__ mówi Pythonowi, co ma zrobić, gdy użyjemy znaku +
    # self  = obiekt po LEWEJ stronie +
    # other = obiekt po PRAWEJ stronie +
    def __add__(self, other):
        return Wektor2D(self.x + other.x, self.y + other.y)

# (-)   # __sub__ mówi Pythonowi, co ma zrobić, gdy użyjemy znaku -
    # self  = wektor po lewej stronie -
    # other = wektor po prawej stronie -
    def __sub__(self, other):
        # odejmujemy x od x oraz y od y
        # wynik zapisujemy jako NOWY obiekt Wektor2D
        return Wektor2D(self.x - other.x, self.y - other.y)

# (==)
       # __eq__ mówi Pythonowi, jak ma porównywać dwa obiekty za pomocą ==
    def __eq__(self, other) -> bool: # Zwraca True tylko gdy x i y są takie same
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str: 
        return f"[{self.x}, {self.y}]"

# Wywołanie 

w1 = Wektor2D(5, 10)
w2 = Wektor2D(2, 4)
w3 = Wektor2D(5, 10)

print(f"Wektor 1: {w1}")
print(f"Wektor 2: {w2}")
print("-" * 30)

# Dodawanie 

suma = w1 + w2
print(f"Suma (w1 + w2): {suma}")

# Odejmowanie 

roznica = w1 - w2 
print(f"Różnica (w1 - w2):  {roznica}")

# porownianie 

print(f"Czy w1 == w2? : {w1 == w2}")
print(f"Czy w1 == w3?: {w1 == w3}")



