# Zadanie 7 
# Bezpieczne pobieranie ze słownika: Napisz funkcję pobierz_wartosc(slownik,
# klucz) , która bezpiecznie zwraca wartość dla danego klucza. Jeśli klucza nie ma, funkcja
# nie powinna rzucać błędu, tylko zwracać None . Zrób to bez użycia try...except
# (wskazówka: metoda .get() ). Następnie napisz drugą wersję z użyciem try...except
# KeyError .

def pobierz_wartosc(slownik, klucz): 
    try: 
        return slownik[klucz]
    except KeyError: 
        return None

slownik = {  
     "iqos": "heets",
     "glo": "rivo",    
    }

print(pobierz_wartosc(slownik, "iqos")) 
print(pobierz_wartosc(slownik, "malboro"))
