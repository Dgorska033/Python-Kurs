## KOD STAROTWY DO ZADAŃ

import sqlite3

def przygotuj_baze():
    conn = sqlite3.connect('sklep.db')
    c = conn.cursor() 

    # Usunięcie tabel, jeśli istnieją, dla czystego startu
    c.execute("DROP TABLE IF EXISTS Zamowienia_Produkty")
    c.execute("DROP TABLE IF EXISTS Zamowienia")
    c.execute("DROP TABLE IF EXISTS Produkty")
    c.execute("DROP TABLE IF EXISTS Kategorie")
    c.execute("DROP TABLE IF EXISTS Klienci")

    c.execute('''--sql
    CREATE TABLE Kategorie(
    id_kategorii INTEGER PRIMARY KEY,
    nazwa_kategorii TEXT UNIQUE NOT NULL
    )
    ''')
    c.execute('''--sql
    CREATE TABLE Produkty(
    id_produktu INTEGER PRIMARY KEY,
    nazwa_produktu TEXT NOT NULL,
    cena REAL NOT NULL, 
    id_kategorii INTEGER,
    FOREIGN KEY (id_kategorii) REFERENCES Kategorie(id_kategorii)
    )''')
    c.execute('''--sql
    CREATE TABLE klienci(
    id_klienta INTEGER PRIMARY KEY,
    imie TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL)
    ''')
    c.execute('''--sql
    CREATE TABLE Zamowienia(
    id_zamowienia INTEGER PRIMARY KEY, 
    id_klienta INTEGER, 
    data_zamowienia DATE,
    FOREIGN KEY (id_klienta) REFERENCES Klienci (id_klienta)
    )
    ''')
    c.execute('''--sql
    CREATE TABLE Zamowienia_Produkty(
    id_zamowienia INTEGER,
    id_produktu INTEGER, 
    ilosc INTEGER NOT NULL, 
    PRIMARY KEY (id_zamowienia, id_produktu),
    FOREIGN KEY (id_zamowienia) REFERENCES Zamowienia(id_zamowienia),
    FOREIGN KEY (id_produktu) REFERENCES Produkty(id_produktu)
    )
    ''')
    #Wstawianie danych
    kategorie = [('Elektronika',), 
                 ('Książki',), 
                 ('Dom i ogród',)]
    klienci  = [('Anna Nowak', 'anna@nexample.com'), 
                ('Jan Kowalski', 'jan.k@example.com'), ('Zofia Wiśniewska', 'zofia.w@example.com')]
    produkty = [
        ('Laptop Pro', 5200.00, 1), ('Smartfon X', 2500.00, 1),
        ('Python dla każdego', 89.99, 2), ('Wzorce projektowe', 120.50, 2),
        ('Kosiarka elektryczna',  750.00, 3), ('Zestaw narzędzi', 300.00, 3),
        ('Słuchawki bezprzewodowe', 450.00, 1)]
    zamowienia = [(1, '2003-10-01'), (2, '2023-10-02'), (1, '2023-10-05')]
    zamowienia_produkty = [(1, 1, 1), (1, 7, 1), (2, 3, 2), (3, 5, 1)]

    c.executemany("INSERT INTO Kategorie (nazwa_kategorii) VALUES (?)", kategorie)
    c.executemany("INSERT INTO Klienci (imie, email) VALUES (?, ?)", klienci)
    c.executemany("INSERT INTO Produkty (nazwa_produktu, cena, id_kategorii) VALUES(?, ? , ?)", produkty)
    c.executemany("INSERT INTO Zamowienia (id_klienta, data_zamowienia) VALUES (?, ?)", zamowienia)
    c.executemany("INSERT INTO Zamowienia_Produkty (id_zamowienia, id_produktu, ilosc) VALUES (?, ?, ?)", zamowienia_produkty)

    conn.commit()
    conn.close() 
    print("Baza 'sklep.db' została przygotowana")

przygotuj_baze() 