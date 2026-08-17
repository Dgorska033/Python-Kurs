# Zadanie 2 – Walidator wieku
# Stwórz klasę Uzytkownik z atrybutem _wiek. Użyj dekoratora @property, aby stworzyć
# właściwość wiek. Getter powinien zwracać wiek, a setter powinien sprawdzać, czy podany
# wiek jest w zakresie od 0 do 120. Jeśli nie jest, powinien wyświetlić komunikat błędu i nie
# zmieniać wartości.


class Uzytkowwnik:
    def __init__(self, wiek: int = 0) -> None:
        self._wiek = wiek
        self.wiek = wiek

    @property
    def wiek(self) -> int:
        """Pobiera wiek użytkownika.

        Returns:
            int: Aktualny wiek użytkownika.
        """
        return self._wiek

    @wiek.setter
    def wiek(self, wiek: int) -> None:
        """Ustawia wiek użytkownika po uprzedniej walidacji zakresu.

        Args:
            wiek (int): Nowy wiek do ustawienia (0 - 120).
        """
        if 0 <= wiek <= 120:
            self._wiek: int = wiek
        else:
            print("[Błąd]: Wiek nie mieści się w przedziale 0 - 120")

user = Uzytkowwnik(-20)
print("Wiek początkowy:", user.wiek)
user.wiek = 130
print("Wiek po próbie zmiany na wartość poza zakresem:", user.wiek)
user.wiek = 119
print("Wiek po udanej zmianie:", user.wiek)


