# Zadanie 5 – Lista klientów
# Napisz skrypt, który wyświetli imiona i adresy e-mail wszystkich klientów z tabeli Klienci

import sqlite3 

conn = sqlite3.connect('sklep.db')
c = conn.cursor() 

c.execute("SELECT imie, email FROM klienci")

wszyscy_klienci = c.fetchall()

print("Klienci:")
for imie, email in wszyscy_klienci:
    print(f"{imie}, email: {email}")

conn.commit()
conn.close()