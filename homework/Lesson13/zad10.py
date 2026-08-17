# Zadanie 10 – Funkcja wyszukująca z JOIN
# Napisz funkcję w Pythonie znajdz_sale_studenta(nazwisko), która przyjmuje nazwisko
# studenta jako argument. Funkcja powinna połączyć się z bazą, a następnie znaleźć i
# wyświetlić informację, w którym budynku i w jakiej sali znajduje się dany student 

import sqlite3

def znajdz_sale_studenta(nazwisko):
    """
    Szukam studenta po nazwisku i zwracam budynek oraz numer sali,
    do której jest przypisany.
    """
    conn = sqlite3.connect('uczelnia.db')
    c = conn.cursor() 

# Chcę znaleźć salę konkretnego studenta.
#
# Problem jest taki, że w tabeli Studenci nie ma informacji o sali.
# Muszę więc przejść przez 3 tabele:
#
# Studenci -> przypisania -> Audytoria
#
# Najpierw znajduję studenta i jego ID.
# Potem po jego ID sprawdzam w "przypisania", jakie ma ID audytorium.
# Na końcu po ID audytorium znajduję budynek i numer sali.
    c.execute('''
        SELECT a.nazwa_budynku, a.numer_sali
        FROM Studenci AS s                      
        JOIN przypisania AS p
            ON p.id_studenta = s.id_studenta
        JOIN Audytoria AS a
            ON p.id_audytorium = a.id_audytorium 
        WHERE s.nazwisko = ?     
    ''', (nazwisko,)) 

   
# JOIN = którą tabelę dołączam
# ON = po jakich kolumnach łączę rekordy
# AS = krótki alias tabeli

# Studenci -> przypisania
# Łączę po id_studenta

# przypisania -> Audytoria
# Łączę po id_audytorium

    wynik = c.fetchone()
    conn.close()
    return wynik


print(znajdz_sale_studenta("Kowalski"))
print(znajdz_sale_studenta("Górska"))
