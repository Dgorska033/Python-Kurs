# Zadanie 6 – Dwie tabele: Studenci i Audytoria
# Napisz skrypt, który w nowej bazie uczelnia.db stworzy dwie tabele:
# studenci z kolumnami: id_studenta (klucz główny), imie (TEXT), nazwisko
# (TEXT).
# audytoria z kolumnami: id_audytorium (klucz główny), nazwa_budynku (TEXT),
# numer_sali (INTEGER).

import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()
print("Połączono z bazą dnaych")

c.execute(
    '''--sql
        CREATE TABLE IF NOT EXISTS Studenci(
        id_studenta INTEGER PRIMARY KEY,
        imie TEXT NOT NULL, 
        nazwisko TEXT NOT NULL
        )
'''
)

c.execute(
    '''--sql
        CREATE TABLE IF NOT EXISTS Audytoria(
        id_audytorium INTEGER PRIMARY KEY, 
        nazwa_budynku TEXT NOT NULL, 
        numer_sali INTEGER
        )
'''
)

conn.commit()
print("Tabele zostały utowrzone")

conn.close()

