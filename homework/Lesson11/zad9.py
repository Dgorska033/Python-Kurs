#  Zadanie 9 – Walidacja danych w init
# Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
# Wewnątrz konstruktora dodaj walidację:
# Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z
# odpowiednim komunikatem.
# Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku
# try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi
# danymi. 


class RejestracjaUzytkownika:
    def __init__(self, email: str , haslo: str):

        if "@" not in email: 
            raise ValueError("Błąd w mailu. Brakuje @")

        if len (haslo) < 8: 
            raise ValueError("Hasło jest za krótkie. Musi zawierać conajmniej 8 znaków")
        
        self.email = email
        self.haslo = haslo
        print("Pomyślnie zarejestrowano użytkownika")

print("\n""======= TEST ======= Niepoprawny mail" "\n")
try: 
    uzytkownik1 = RejestracjaUzytkownika("stas.123.pl", "bezpiecznehaslo123" "\n")

except ValueError as e:
    print(f"Przechwycono wyjątek {e}")

            
print("\n""========= TEST ========== Hasło za krótkie \n")

try: 
    uzytkownik2 = RejestracjaUzytkownika("stas.123@.pl", "stas12" "\n")

except ValueError as e:
    print(f"Przechwycono wyjątek {e}")


print("\n""============== TEST ========== Poprawne dane" "\n")

try: 
    uzytkownik3 = RejestracjaUzytkownika("stas.123@.pl", "bezpiecznehaslo123" "\n")

except ValueError as e:
    print(f"Przechywcono wyjątek {e}")

