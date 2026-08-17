# import sqlite3

# conn = sqlite3.connect('kurs.db')
# c = conn.cursor()
# # print("Połączono z bazą danych!")

# # conn.close(
# # 
# # c.execute(
# #     '''--sql
# #     CREATE TABLE IF NOT EXISTS miasta (
# #     id INTEGER PRIMARY KEY, 
# #     nazwa  TEXT NOT NULL,
# #     populacja INTEGER
# #     )
# # '''
# # )             

# # conn.commit()

# # print("Tabela została utworzona.")

# # conn.close()

# c.execute("INSERT INTO miasta (nazwa, populacja) VALUES (?, ?)", ('Warszawa', 1794166))
# # rekordy = c.rowcount
# c.execute("INSERT INTO miasta (nazwa, populacja) VALUES (?, ?)", ('Kraków', 779996))
# # rekordy1 = c.rowcount


# miasta_do_dodania = [
#     ('Łódź', 679941),
#     ('Wrocław', 642869),
#     ('Poznań', 534813)
# ]

# c.executemany("INSERT INTO miasta (nazwa, populacja) VALUES (?, ?)", miasta_do_dodania)


# conn.commit()

# # rekordy3 = c.rowcount

# # suma_rekordy = rekordy + rekordy1 + rekordy3
# print(f"Dodawno {conn.total_changes} rekordy do tabeli")

# conn.close()

# import sqlite3 

# conn = sqlite3.connect('kurs.db')
# c = conn.cursor() 

# c.execute("SELECT * FROM miasta")

# wszystkie_miasta = c.fetchall() 
# print("Wszystkie miasta w bazie: ")
# for miasto in wszystkie_miasta:
#     print(miasto)

# print("\nMiasta z populacją powyżej 700 000: ")
# c.execute("SELECT nazwa, populacja FROM miasta WHERE populacja > ?", (700000,))

# miasta_powyzej_700k = c.fetchall()
# for miasto in miasta_powyzej_700k:
#     print(f"- {miasto[0]}, populacja: {miasto[1]}")

# conn.close() 




# import sqlite3 

# conn = sqlite3.connect('kurs.db')
# c = conn.cursor() 

# nowa_populacja = 54000
# miasto_do_aktualizacji = 'Poznań'

# c.execute("UPDATE miasta SET populacja = ? WHERE nazwa = ?", (nowa_populacja, miasto_do_aktualizacji))
# conn.commit()

# print(f"Zaktualizowano populację dla miasta: {miasto_do_aktualizacji}.Zmieniono {c.rowcount} rekordów.")

# c.execute("SELECT * FROM miasta WHERE nazwa = ?", (miasto_do_aktualizacji,))
# zaktualizowane_miasto = c.fetchone() 

# print(f"Nowe dane {zaktualizowane_miasto}")

# conn.close()

