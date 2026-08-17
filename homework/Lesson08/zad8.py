# Zadanie 8
# Walidacja hasła v2: Rozbuduj funkcję do walidacji hasła. Powinna ona zwracać listę
# wszystkich błędów walidacji, zamiast rzucać wyjątkiem po pierwszym napotkanym
# problemie. Jeśli lista błędów nie jest pusta, rzuć własnym wyjątkiem BladWalidacjiError ,
# przekazując do niego tę listę.

import string 

# Komnikaty błędów walidacji
PASSWORD_OK: str = "Hasło spełnia wszystkie wymagania"
PASSWORD_MIN_LENGHT: str = "Hasło musi mieć co najmniej 8 znaków" 
PASSWORD_NO_DIGIT: str = "Hasło musi zawierać co najmniej jedną cyfrę"
PASSWORD_NO_UPPERCASE: str = "Hasło musi zawierać co najmniej jedną wielką literę"
PASSWORD_NO_LOWERCASE: str = "Hasło musi zawierać co najmniej jedną małą literę"
PASSWORD_NO_SPECIAL: str = "Hasło musi zawierać co najmniej jeden znak specialny" 

class BladWalidacjiError(Exception): 
    pass

def waliduj_haslo(haslo: str) -> None: 
    """
    Sprawdza haslo pod kątem wymagań. 
    Hasło (str) > hasło do sprawdzenia 
    Raises: 
        BladWalidacjiError: jeśli haslo nie spelnia wymagań, przekazuje listę błędów walidacji
    
    """
    bledy: list[str] = [] 

    if len(haslo) < 8: 
        bledy.append(PASSWORD_MIN_LENGHT) 

    if not any(char.isdigit() for char in haslo): 
        bledy.append(PASSWORD_NO_DIGIT) 

    if not any(char.isupper() for char in haslo): 
        bledy.append(PASSWORD_NO_UPPERCASE) 

    if not any(char.islower() for char in haslo): 
        bledy.append(PASSWORD_NO_LOWERCASE) 

    if not any(char in string.punctuation for char in haslo): 
        bledy.append(PASSWORD_NO_SPECIAL) 

    if bledy: 
        raise BladWalidacjiError(bledy) 

    print(PASSWORD_OK) 

try: 
    waliduj_haslo("duPA ") 
except BladWalidacjiError as e: 
    print("Hasło:") 
    for uwaga in e.args[0]:
        print(f"-{uwaga}")
