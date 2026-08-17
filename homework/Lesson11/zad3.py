#  Zadanie 3 – Dziedziczenie Pracownik -> Programista
# Stwórz klasę bazową Pracownik z atrybutami imie i stawka_godzinowa. Dodaj metodę
# oblicz_pensje(liczba_godzin). Następnie stwórz klasę potomną Programista, która
# dziedziczy po Pracownik. W klasie Programista dodaj atrybut jezyki_programowania (lista
# stringów). Stwórz obiekt klasy Programista i wywołaj na nim metodę oblicz_pensje

#Klasa bazowa (rodzic)
class Pracownik:
    def __init__(self, imie, stawka_godzinowa):
        self.imie = imie
        self.stawka_godzinowa = stawka_godzinowa

  # liczba_godzin nie jest atrybutem obiektu - podajemy ją dopiero przy wywołaniu metody
    def oblicz_pensje(self, liczba_godzin):
        return self.stawka_godzinowa * liczba_godzin
    
# Programista dziedziczy po Pracownik, więc dostaje jego atrybuty i metody
class Programista(Pracownik):
    # Podajemy tutaj ponownie self, imie i stawka_godzinowa,
    # ponieważ tworząc obiekt Programista, ten __init__ musi przyjąć wszystkie jego dane.
    # imie i stawka_godzinowa pochodzą z klasy Pracownik,
    # a jezyki_programowania to nowy atrybut dodany przez klasę Programista.
        def __init__(self, imie, stawka_godzinowa, jezyki_programowania): 
        # super() odwołuje się do klasy rodzica, czyli tutaj do Pracownik.
        #  Wywołujemy __init__ klasy Pracownik (rodzica)
        # Dzięki temu nie musimy ponownie pisać:
        #  self.imie = imie
        #  self.stawka_godzinowa = stawka_godzinowa
            super().__init__(imie, stawka_godzinowa)
            self.jezyki_programowania = jezyki_programowania


# lista = znane języki
pracownik1 = Programista("Kamil", 78, ["Python", "JavaScript"])

# 140 przekazujemy do parametru liczba_godzin w metodzie oblicz_pensje()
# Programista może użyć tej metody, ponieważ odziedziczył ją po Pracownik
print(f"Zarobiłeś {pracownik1.oblicz_pensje(140)} zł brutto")



# Jeśli klasa potomna ma własny __init__, używam super().__init__(...)
# żeby uruchomić __init__ rodzica i ustawić odziedziczone atrybuty.