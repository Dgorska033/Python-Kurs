# Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki

from dataclasses import dataclass

class BrakSrodkowError(Exception): ...

@dataclass
class BankAccount:
    _saldo : float
    
    @property
    def saldo(self) -> float:
        return self._saldo

    def wplac(self, kwota: float):
       if kwota < 0: 
           raise ValueError("Nie można wpłacić ujemnej kwoty")
       self._saldo += kwota
       return self._saldo

    def wyplac(self, kwota: float):
        if kwota < 0: 
            raise ValueError("Nie można wypłacić ujemnej kwoty")
        elif self._saldo < kwota:
            raise BrakSrodkowError("Brak środków na koncie")
        self._saldo -= kwota
        return self._saldo


print("=========TEST 1: wszytsko ok============")

try: 
    konto = BankAccount(8500)
    wplata = konto.wplac(550)
    print(f"Twoje konto po włacie: {wplata} PLN")

    wyplata = konto.wyplac(1000)
    print(f"Twoje konto po wypłacie: {wyplata} PLN \n")

except ValueError as e:
    print(f"{e}")
except BrakSrodkowError as e:
        print(f"{e}")



print("\n =========TEST 2: wpłata ujemnej kwoty============ \n")


try: 
    konto = BankAccount(8500)
    wplata = konto.wplac(-50)
    print(f"Twoje konto po włacie: {wplata} PLN")

except ValueError as e:
    print(f"{e}")
except BrakSrodkowError as e:
        print(f"{e} \n")


print("\n =========TEST 3: Wyłata ujemnej kwoty============ \n")

try: 
    konto = BankAccount(8500)
    wyplata = konto.wyplac(-300)
    print(f"Twoje konto po wypłacie: {wyplata} PLN \n")
except ValueError as e:
    print(f"{e}")
except BrakSrodkowError as e:
        print(f" {e} \n")



print("\n =========TEST 4: Saldo mniejsze niż wypłata============ \n")

try: 
    konto = BankAccount(1500)
    wyplata = konto.wyplac(2000)
    print(f"Twoje konto po wypłacie: {wyplata} PLN")

except ValueError as e:
    print(f"{e}")
except BrakSrodkowError as e:
    print(f"{e}")

