#  Zadanie 3 – Wyświetl całą bibliotekę
# Napisz skrypt, który pobierze i wyświetli w konsoli wszystkie książki (wszystkie kolumny) z
# tabeli ksiazki

import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

c.execute("SELECT * FROM tabela_ksiazek")

wszystkie_ksiazki = c.fetchall()
print("Wszystkie książki w bazie: ")

for ksiazka in wszystkie_ksiazki:
    print(ksiazka)

conn.commit()
conn.close()

