# Zadanie 7 – Wypełnij dane uczelni
# Napisz skrypt, który wypełni tabele studenci i audytoria przykładowymi danymi. Dodaj co
# najmniej 4 studentów i 3 audytoria.

import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

studenci_do_doania = [
("Jan", "Kowalski"), 
("Maria", "Składowska"), 
("Dominika", "Górska"),
("Krystain", "Nowak")
]

c.executemany("INSERT INTO Studenci (imie, nazwisko) VALUES (? , ?)", (studenci_do_doania))
conn.commit()

print(f"Dodawno {c.rowcount} rekordy do tabeli")

audytoria_do_dodania = [
("Szkoła1", 56),
("Szkoła1", 123),
("Szkoła3", 54)
]

c.executemany("INSERT INTO Audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)", (audytoria_do_dodania))
conn.commit()

print(f"Dodawno {c.rowcount} rekordy do tabeli")

print(f"Wszystkie {conn.total_changes} rekordy dodane do tabeli")

conn.close()

