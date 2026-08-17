# Zadanie 5 – Zaktualizuj rok wydania
# Wybierz jedną z dodanych książek i napisz skrypt, który zaktualizuje jej rok_wydania na
# inną wartość. Po aktualizacji wyświetl dane tej książki, aby potwierdzić, że zmiana się
# powiodła.

import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

nowy_rok_wydania = 2021
ksiazka_do_aktualizacji = "50 Wielkich Idei"
autor_ksiazki = "Ben Dupre"

c.execute("UPDATE tabela_ksiazek SET rok_wydania = ? WHERE tytuł = ? AND autor = ?", 
          (nowy_rok_wydania, ksiazka_do_aktualizacji, autor_ksiazki))
conn.commit()

print(f"Zaktualizowano rok wydania dla książki: {ksiazka_do_aktualizacji}.Zmieniono {c.rowcount} rekordów.")


c.execute("SELECT * FROM tabela_ksiazek WHERE tytuł = ?", (ksiazka_do_aktualizacji,))
zaktualizowana_ksiazka = c.fetchone()
print(f"Zaktualizowna ksiązka {zaktualizowana_ksiazka}")

conn.close()

