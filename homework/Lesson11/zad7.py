#  Zadanie 7 – Enkapsulacja w Telewizorze
# Stwórz klasę Telewizor. Użyj enkapsulacji, aby ukryć następujące atrybuty: kanal
# (domyślnie 1), glosnosc (domyślnie 10), __wlaczony (domyślnie False). Stwórz publiczne
# metody do zarządzania telewizorem:
# wlacz() i wylacz()
# zmien_kanal(numer) : kanał można zmienić tylko, gdy TV jest włączony.
# glosniej() i ciszej() : głośność można regulować w zakresie 0-100 i tylko, gdy TV
# jest włączony.
# info(): wyświetla aktualny stan (włączony/wyłączony, kanał, głośność). Przetestuj, czy
# nie da się zmienić kanału na wyłączonym telewizorze lub ustawić głośności powyżej
# 100. (challenge)

class Tv:
    def __init__(self, kanal=1, glosnosc=10, wlaczony=False):
        # Prywatne atrybuty - enkapsulacja
        self.__kanal = kanal
        self.__glosnosc = glosnosc
        self.__wlaczony = wlaczony

        # Jedna flaga sprawdzająca, czy komunikat już się pojawił
        self.__komunikat_pokazany = False

    def wlacz(self):
        self.__wlaczony = True

        # Reset flagi
        self.__komunikat_pokazany = False

    def wylacz(self):
        self.__wlaczony = False

        # Reset flagi
        self.__komunikat_pokazany = False


    # Zmienia kanał tylko, gdy TV jest włączony
    def zmien_kanal(self, number):
        if self.__wlaczony:
            self.__kanal = number
            self.__komunikat_pokazany = False

        elif not self.__komunikat_pokazany:
            print("TV wyłączone. Nie można zmienić kanału")
            self.__komunikat_pokazany = True


    # Zwiększa głośność o 1, maksymalnie do 100
    def glosniej(self):
        if self.__wlaczony:

            if self.__glosnosc < 100:
                self.__glosnosc += 1
                self.__komunikat_pokazany = False

            elif not self.__komunikat_pokazany:
                print("Głośność jest na maksimum")
                self.__komunikat_pokazany = True

        elif not self.__komunikat_pokazany:
            print("TV jest wyłączone.")
            self.__komunikat_pokazany = True


    # Zmniejsza głośność o 1, minimalnie do 0
    def ciszej(self):
        if self.__wlaczony:

            if self.__glosnosc > 0:
                self.__glosnosc -= 1
                self.__komunikat_pokazany = False

            elif not self.__komunikat_pokazany:
                print("TV jest maksymalnie wyciszony")
                self.__komunikat_pokazany = True

        elif not self.__komunikat_pokazany:
            print("TV jest wyłączone. Nie można ściszyć")
            self.__komunikat_pokazany = True


    # Wyświetla aktualny stan TV
    def info(self):
        state = "włączone" if self.__wlaczony else "wyłączone"

        if self.__wlaczony:
            print(
                f"TV jest {state}, kanał: {self.__kanal}, "
                f"głośność: {self.__glosnosc}"
            )
        else:
            print(f"TV jest {state}")


# Funkcja pomocnicza - wykonuje daną funkcję wiele razy
def reapeter(times, func):
    def wraper(*args, **kwargs):
        for i in range(times):
            func(*args, **kwargs)

    return wraper


# ---------------- TEST ----------------

tv = Tv()

tv.wlacz()

# Podgłaśniam 100 razy
powtorz_glosniej = reapeter(100, tv.glosniej)
powtorz_glosniej()

tv.zmien_kanal(15)
tv.info()

# -------------------------------------------
print("-" * 30)
#--------------------------------------------
# Wyłączamy TV
tv.wylacz()

# Repeater próbuje podgłośnić 15 razy,
# ale komunikat wyświetli się tylko raz
powtorz_glosniej = reapeter(15, tv.glosniej)
powtorz_glosniej()

tv.zmien_kanal(15)
tv.info()
