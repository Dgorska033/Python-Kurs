# Zadanie 6 

# Wielokrotne powitanie: Napisz funkcję wielokrotne_powitanie(imie: str, ilosc:
# int) -> None , która wyświetla powitanie f"Cześć, {imie}!" tyle razy, ile wynosi
# ilosc . Ta funkcja nie powinna niczego zwracać

def powitanie(imie: str, ilosc: int) -> None:
   print(f"Cześć, {imie}! " * ilosc)

powitanie("Dominika", 5)
