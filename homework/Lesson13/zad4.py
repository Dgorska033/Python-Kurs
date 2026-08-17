# Zadanie 4 – Wyszukaj książki autora
# Napisz skrypt, który pobierze i wyświetli tylko te książki z tabeli ksiazki, które zostały
# napisane przez Twojego ulubionego autora


import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

c.execute("SELECT tytuł, autor, rok_wydania FROM tabela_ksiazek WHERE autor is ?", ("Richard Dawkins",))


wszystkie_ksiazki = c.fetchall()
print("Ksiązki z bazy napisane przez mojego ulubionego autora: ")
for ksiazka in wszystkie_ksiazki:
    print(ksiazka)

conn.commit()
conn.close()

