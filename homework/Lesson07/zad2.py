# Zadanie 2 - 
# Sortowanie słownika: Masz słownik oceny = {"Jan": 4, "Anna": 5, "Piotr": 3,
# "Kasia": 4} . Użyj funkcji sorted() i funkcji lambda, aby posortować elementy
# słownika (klucz, wartość) według ocen (od najwyższej do najniższej)


oceny = {"Jan": 4, "Anna": 5, "Piotr": 3, "Kasia": 4}

posortowane_oceny = sorted(oceny.items(), key=lambda element: element[1], reverse=True)  
# items() pobiera pary imię-ocena, lambda wybiera ocenę [1], [0] to by było imię reverse=True odwraca kolejność na malejącą.
# lambda może zawierać tylko jedno wyrażenie, dobra do krótkich operacji
print(posortowane_oceny)

