# Zadanie 4
# Znajdowanie liczb pierwszych: Użyj funkcji filter() , aby z listy liczb od 1 do 30 wybrać
# tylko liczby pierwsze. (Wskazówka: napisz pomocniczą funkcję czy_pierwsza(n) , która
# sprawdza, czy liczba jest pierwsza)

def czy_pierwsza(n): 
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False      
    return True

"""
Liczby mniejsze od 2 nie są liczbami pierwszymi
Sprawdzamy po kolei liczby od 2 do n-1
i sprawdzamy, czy któraś jest dzielnikiem n
% sprawdza resztę z dzielenia.
Jeśli n da się podzielić przez i i nic nie zostanie,
to znaleźliśmy dodatkowy dzielnik, więc liczba nie jest pierwsza
Jeśli pętla nie znalazła żadnego dzielnika, liczba jest pierwsza
""" 
liczby = range(1,31) #zakres liczb do sprawdzenia

# filter sprawdza każdą liczbę za pomocą funkcji czy_pierwsza.
# Zostawia tylko te, dla których funkcja zwróci True.
# # # list() zamienia wynik filter na zwykłą listę.
liczby_pierwsze = list(filter(czy_pierwsza, liczby))
print(liczby_pierwsze) 



