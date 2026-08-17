# Zadanie 10 – Metaklasa walidująca
# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
# wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
# docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
# informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
# niepoprawnie udokumentowanymi metodami

class MetaWalidujMetody(type):

    def __new__(cls, nazwa, klasy_bazowe, przestrzen_nazw):

        for nazwa_metody, wartosc in przestrzen_nazw.items():

            # Pomijamy metody magiczne, np. __init__
            if nazwa_metody.startswith("__"):
                continue

            # Sprawdzamy tylko metody
            if callable(wartosc):

                # __doc__ zawiera docstring funkcji
                if wartosc.__doc__ is None:
                    raise TypeError(
                        f"Metoda '{nazwa_metody}' wymaga docstringa"
                    )

        return super().__new__(cls, nazwa, klasy_bazowe, przestrzen_nazw)


print("========== POPRAWNA KLASA ==========")


class PoprawnaKlasa(metaclass=MetaWalidujMetody):

    def metoda_1(self):
        """To jest dokumentacja metody 1."""
        print("Metoda 1 działa")

    def metoda_2(self):
        """To jest dokumentacja metody 2."""
        print("Metoda 2 działa")


obiekt = PoprawnaKlasa()
obiekt.metoda_1()
obiekt.metoda_2()


print("========== NIEPOPRAWNA KLASA ==========")


try:

    class NiepoprawnaKlasa(metaclass=MetaWalidujMetody):

        def poprawna_metoda(self):
            """Ta metoda posiada docstring."""
            print("Poprawna metoda")

        def metoda_bez_docstringa(self):
            print("Brak dokumentacji")

except TypeError as blad:
    print(f"Błąd: {blad}")

    