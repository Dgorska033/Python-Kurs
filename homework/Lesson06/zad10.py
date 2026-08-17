# Zadanie 10
# Mini-projekt: Walidator hasła: Stwórz funkcję sprawdz_haslo(haslo: str) -> bool .
# Funkcja powinna sprawdzać, czy hasło spełnia następujące warunki i zwracać True lub
# False :
# Ma co najmniej 8 znaków.
# Zawiera co najmniej jedną wielką literę.
# Zawiera co najmniej jedną cyfrę. Napisz do niej pełną dokumentację (docstring i
# adnotacje).

def sprawdz_haslo(haslo:str) -> bool: 
    """
   Sprawdza, czy podane hasło:
    - ma co najmniej 8 znaków,
    - zawiera co najmniej jedną wielką literę,
    - zawiera co najmniej jedną cyfrę.

    Zwraca True, jeśli wszystkie warunki są spełnione,
    w przeciwnym razie False.
    """

    return( 
        len(haslo) >= 8      #jesli dlugosc hasła wynosi 8 lub wiecej znakow
        and any(litera.isupper() for litera in haslo)  #jesli jakakolwiek litera jest wielka
        and any(cyfra.isdigit() for cyfra in haslo)    # jesli jest jakakolwiek cyfra  
    )
        
przyklady = ["PraPra123" ,  # True
             "ZbzB091a",    # True
             "AbcdD1a5",    # True
             "21345a",      # False
             "Ala1",        # False
             "abcekhf1",    # False
            "123#@Ak"       # False
]

for tekst in przyklady:
    print(sprawdz_haslo(tekst))
"""
Na koniec sprawdzenie waerości z podanej listy przykładów, czy warunki zostały spełnione.

"""

