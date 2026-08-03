# Zadanie 2:

# Walidator wieku: Stwórz funkcję rejestruj_uzytkownika(wiek) , która rzuca własnym,
# zdefiniowanym przez Ciebie wyjątkiem WiekNiepoprawnyError , jeśli wiek jest mniejszy niż
# 18. Napisz kod, który wywołuje tę funkcję i obsługuje ten wyjątek

class WiekNiepoprawnyError(Exception):  # żeby błąd zadziałał musze go stworzyć?? 
    pass


def rejestruj_uzytkownika(wiek: int): 
    try : 
        if wiek < 18: 
            raise WiekNiepoprawnyError # musi być pełnoletni hehe / wywoływanie błedu 
        elif wiek > 150: 
            raise ValueError("Jesteś wampirem")
        elif wiek >= 18: 
            print("Wszystko ok")

    except WiekNiepoprawnyError as e:   
        print(f"Nie sprzedam Ci monsterka {e}")

rejestruj_uzytkownika(17)


# Tutaj zrobiłam sobie z inputem
# def rejestruj_uzytkownika(): 
#     try : 
#         wiek = int(input("Ile masz lat?: "))
#         if wiek < 18: 
#             raise WiekNiepoprawnyError # musi być pełnoletni hehe / wywoływanie błedu 
#         elif wiek > 150: 
#             raise ValueError("Jesteś wampirem")
#         elif wiek >= 18: 
#             print("Wszystko ok")

#     except WiekNiepoprawnyError as e:   
#         print(f"Nie sprzedam Ci monsterka {e}")

# rejestruj_uzytkownika()

