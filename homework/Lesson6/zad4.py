# Zadanie 4 
# Sprawdzanie zakresu: Zdefiniuj zmienną globalną POZIOM_DOSTEPU = "user" . Napisz
# funkcję, która próbuje zmienić tę zmienną na "admin" bez użycia słowa kluczowego
# global . Wewnątrz funkcji stwórz zmienną lokalną o tej samej nazwie. Wyświetl wartość
# zmiennej wewnątrz i na zewnątrz funkcji, aby zobaczyć różnicę

LEVEL_ACCES = "user" 

def zmieniona_nazwa(admin):
    admin == "user"
    print(admin)   # Zmieniona nazwa działa tylko wewnątrz funkcji bo jest zmieniona tylko lokalnie, admin: wartość user

print(zmieniona_nazwa("admin")) # Globalnie nazwa nie jest zdefiniowana więc wyświetla wartość None
