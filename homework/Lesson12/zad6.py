# Zadanie 6 – Własny wyjątek InvalidPasswordError
# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
# która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
# (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
# testuje tę funkcję w bloku try...except.

class InvalidPasswordError(Exception): ...

def create_password(password: str):
    try:
        if len (password) < 8:
            raise InvalidPasswordError("Password to short. Must contain min. 8 characters")

        return "Passowrd sucesfully created"

    except InvalidPasswordError as e:
        print(f"Error found: {e}")

print("\n =======TEST - password corecct =======")
print(create_password("mama.123"))

print("\n =======TEST - password incorecct =======")

print(create_password("mama12"))
