#  Zadanie 4 – Czytelny Punkt
# Stwórz klasę Punkt do reprezentowania punktu w 2D, z atrybutami x i y. Zaimplementuj
# metodę str, aby print(punkt) wyświetlał współrzędne w formacie (x, y)

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# implementacja metody __str__
    def __str__(self):    #  # Ta metoda musi zwrócić stringa
        return f'{self.x}, {self.y}'

wspolrzedne1 = Punkt("52°13'N", "21°00'E")  # Współrzędne podjamy w "" bo to stringi
wspolrzedne2 = Punkt("35°41'N", "139°46'E")
print(f"Współrzędne geograficzne Warszawy: {wspolrzedne1}")  
print(f"Współrzędne geograficzne Tokio: {wspolrzedne2}")  
