#  Zadanie 1 – Stwórz tabelę książek
# Napisz skrypt, który połączy się z bazą biblioteka.db i stworzy w niej tabelę ksiazki. Tabela
# powinna mieć następujące kolumny:
# id (INTEGER, klucz główny)
# tytul (TEXT, nie może być pusty)
# autor (TEXT, nie może być pusty)
# rok_wydania (INTEGER)

import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()
print("Połączono z bazą danych!")


c.execute(
    '''--sql
    CREATE TABLE IF NOT EXISTS tabela_ksiazek(
    id INTEGER PRIMARY KEY,
    tytuł TEXT NOT NULL, 
    autor TEXT NOT NULL,
    rok_wydania INTEGER
    )
'''
)

conn.commit()

print("Tabela została utworzona")

conn.close()
