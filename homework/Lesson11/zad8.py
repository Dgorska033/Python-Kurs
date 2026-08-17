# Zadanie 8 – Hierarchia instrumentów muzycznych
# Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
# Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
# która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę
# metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą
# super().graj().
# Instrument.graj() -> "Wydaje dźwięk."
# Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
# Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]" (challenge)

class Instrument:
    def __init__(self, nazwa):
        self.nazwa = nazwa

    def graj (self):
        return f"Instrument: {self.nazwa} : Gram! :"

class Strunowy(Instrument):
    def graj(self):
        return f"{super().graj()} Szarpię struny."

class Dety(Instrument):
    def graj(self):
        return f"{super().graj()} Wydaję dmuchane dźwięki."

class Gitara(Strunowy):
    def graj(self):
        return f"{super().graj()} Wydaję dźwięki basowe"

class Trabka(Dety):
    def graj(self):
        return f"{super().graj()} Możesz usłyszeć metaliczne brzemiania"


instrument1 = Instrument("Ogólny instruemnt")
instrument2 = Strunowy("Skrzypce")
instrument3 = Dety("Dudy")
instrument4 = Gitara("Basowa")
instrument5 = Trabka("Klasyczna")

print(instrument1.graj())
print(instrument2.graj())
print(instrument3.graj())
print(instrument4.graj())
print(instrument5.graj())

