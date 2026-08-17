# Zadanie 3 – Konwerter Walut
# Stwórz klasę KalkulatorWalut. Dodaj w niej metodę statyczną (@staticmethod) o nazwie
# usd_na_pln, która przyjmuje kwotę w dolarach i zwraca ją przeliczoną na złotówki (przyjmij
# stały kurs, np. 1 USD = 4.0 PLN). Wywołaj tę metodę bez tworzenia obiektu klasy.


class KalkulatorWalut:
    @staticmethod
    def usd_na_pln(kwota: float):
      return kwota * 4.0


# metoda statyczna - przy @static metod nie tworzę obiektu. Wywołuję metodę bezpośrednio przez nazwę klasy
print(f"Kwota to:  {KalkulatorWalut.usd_na_pln(10)} PLN")
print(f"Kwota to: {KalkulatorWalut.usd_na_pln(20)} PLN")

