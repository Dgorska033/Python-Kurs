# Zadanie 2 – Dodaj książki
# Napisz skrypt, który doda do tabeli ksiazki (stworzonej w zadaniu 1) trzy dowolne książki.
# Użyj metody executemany do dodania wszystkich książek za jednym razem.

import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

ksiazki_do_dodania = [
('Bóg Urojony', 'Richard Dawkins', 2006),
('White Nights', 'Fyodor Dostoyevsky', 1848),
('50 Wielkich Idei', 'Ben Dupre', 2020)
]

c.executemany("INSERT INTO tabela_ksiazek (tytuł, autor, rok_wydania) VALUES (?, ?, ?)", (ksiazki_do_dodania))

conn.commit()

print(f"Dodawno {conn.total_changes} rekordy do tabeli")

conn.close()

