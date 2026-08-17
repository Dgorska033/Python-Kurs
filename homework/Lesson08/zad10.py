# Zadanie 10
# Mini-projekt: Sumator liczb z pliku: Napisz program, który:
# a. Pyta użytkownika o nazwę pliku.
# b. Otwiera plik i czyta go linia po linii.
# c. Każdą linię próbuje przekonwertować na liczbę i dodać do sumy.
# d. Ignoruje linie, których nie da się przekonwertować na liczbę (obsługa ValueError).
# e. Obsługuje FileNotFoundError, jeśli plik nie istnieje.
# f. Na końcu, w bloku finally, wyświetla obliczoną sumę (nawet jeśli wystąpiły błędy po
# drodze)

plik = input("Podaj nazwę pliku: ") 
suma = 0

try:  
    with open(plik, "r") as f: 
        for linia in f:       
            try: 
                linia = int(linia.strip()) # usuwa przestrzenie
                suma += linia
            except ValueError:
                pass # nic z tym nie rób, skipnij dalej
except FileNotFoundError: 
    pass
finally:
    print(f"Suma liczb wynosi: {suma}")


#  cd "D:\Python Kurs\homework\Lesson8"  - polecenie do terminala, bo trzeba wejśc w konkerntą scizke/ plik w terminalu 

