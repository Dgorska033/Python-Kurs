# Zadanie 7 
# Bezpieczne pobieranie ze słownika: Napisz funkcję pobierz_wartosc(slownik,
# klucz) , która bezpiecznie zwraca wartość dla danego klucza. Jeśli klucza nie ma, funkcja
# nie powinna rzucać błędu, tylko zwracać None . Zrób to bez użycia try...except
# (wskazówka: metoda .get() ). Następnie napisz drugą wersję z użyciem try...except
# KeyError .

def pobierz_wartosc(slownik, klucz):
    return slownik.get(klucz) 
""" 
parametr (klucz) > nazwa zmiennej w definicji funkcji,
argument("iqos") > konkretna wartośśc przekazana podczas wywołania.
get(klucz) = znajdź wartość przypisaną do tego klucza
"""

slownik = {  
     "iqos": "heets",
     "glo": "rivo",    
    }

print(pobierz_wartosc(slownik, "iqos")) # heets, słownik + klucz = iqos a wartością przypisaną jest heets XD
print(pobierz_wartosc(slownik, "glo"))  # rivo > analogicznie
print(pobierz_wartosc(slownik, "malboro"))  # None - brak klucza w słowniku 


#.get() - nie wyrzuca bledu jeśli klucz nie istnieje, tylko zwraca None.





