# Zadanie 10

# Mini-projekt: Przetwarzanie danych: Masz listę słowników reprezentujących
# użytkowników:
# Napisz jednolinijkowy kod (używając kombinacji filter , map lub list comprehension),
# który zwróci listę imion aktywnych użytkowników, którzy mają 18 lat lub więcej, pisanych
# wielkimi literami.



uzytkownicy = [
{"imie": "Jan", "wiek": 30, "aktywny": True},
{"imie": "Anna", "wiek": 17, "aktywny": False},
{"imie": "Piotr", "wiek": 25, "aktywny": True},
{"imie": "Kuba", "wiek": 18, "aktywny": False},
{"imie": "Ewa",  "wiek": 9, "aktywny": True}
]

active= list(map(lambda x: x.upper(), [slownik["imie"] for slownik in uzytkownicy if slownik["aktywny"] and slownik["wiek"] >= 18]))
print(active)

