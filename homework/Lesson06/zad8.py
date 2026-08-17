# # Zadanie 8 - 
#  Tworzenie profilu: Napisz funkcję stworz_profil(imie, **dane_dodatkowe) , która
# przyjmuje imię oraz dowolną liczbę nazwanych argumentów (np. wiek=30 ,
# miasto="Warszawa" ). Funkcja powinna zwrócić słownik z profilem użytkownika, gdzie
# klucz 'imie' jest obowiązkowy, a reszta danych jest pobierana z **dane_dodatkowe 

def stworz_profil(imie, **dane_dodatkowe ):
    profil_uzytkownika = {"imie": imie, **dane_dodatkowe}  # tworzę profil, a potem wymieniam w słowniku co się w nim znajduje
    return profil_uzytkownika

print(stworz_profil("Dominika", miasto= "Warszawa" , wiek=23, płeć="kobieta")) 
"""
Dzięki tej funkcji, python zwraca wszystkie dane dodatkowe.
Możemy dodawać do listy, wszystkie dane dodatkowe i nie zwróci błędu.

"""
