# Zadanie 7 – Alternatywny konstruktor dla Daty
# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
# nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
# tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date):
        day, month, year = date.split("-")

        day = int(day)
        month = int(month)
        year = int(year)

        return cls(day, month, year)


    def __str__(self):
        return f"{self.day:02d}-{self.month:02d}-{self.year}"

actual_date = Date.from_string("16-08-2026")
print(actual_date)

