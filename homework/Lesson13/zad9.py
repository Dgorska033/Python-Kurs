# Zadanie 9 – Dokonaj przypisań
# Napisz skrypt, który dokona przypisań. Dla każdego studenta z tabeli studenci dodaj wpis
# do tabeli przypisania, łącząc go z jednym z audytoriów.


import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()


# Pobieranie wszystkich studentów z tabeli Studenci
c.execute("SELECT * FROM Studenci")
wszyscy_studenci = c.fetchall()

# Pobranie wszystkich dostępnych audyrotii
c.execute("SELECT * FROM Audytoria")
wszystkie_sale = c.fetchall()

# enumerate numeruje studentów po kolei.
# "i" to numer, na którym aktualnie jesteśmy: 0, 1, 2, 3...
# "student" to aktualny student z listy.
for i, student in enumerate(wszyscy_studenci):

    
    # Chcemy rozdawać studentom sale po kolei:
    # student 0 -> sala 0
    # student 1 -> sala 1
    # student 2 -> sala 2
    #
    # Ale mamy tylko 3 sale. Nie istnieje sala[3].
    # Dlatego po wykorzystaniu ostatniej sali musimy wrócić do sala[0].
    #
    # % (modulo) daje resztę z dzielenia.
    # Dzięki temu numery sal robią takie kółko:
    #
    # 0 % 3 = 0
    # 1 % 3 = 1
    # 2 % 3 = 2
    # 3 % 3 = 0  -> wracamy do pierwszej sali
    # 4 % 3 = 1
    # 5 % 3 = 2
    #
    # Czyli zamiast 0,1,2,3,4,5...
    # dostajemy ciągle 0,1,2,0,1,2...
    sala = wszystkie_sale[i % len(wszystkie_sale)]

  # student[0] = ID aktualnego studenta
    # sala[0] = ID przydzielonej mu sali
    #
    # Zapisujemy te dwa ID do tabeli "przypisania"
    c.execute("INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)", 
              (student[0], sala[0]))

conn.commit()

print(f"Wszystkie {conn.total_changes} rekordy dodane do tabeli")

conn.close()

