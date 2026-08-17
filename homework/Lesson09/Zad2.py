# Zadanie 2
# Licznik słów: Stwórz program, który pyta o nazwę pliku, odczytuje go, a następnie zlicza i
# wyświetla całkowitą liczbę słów w tym pliku. Obsłuż błąd FileNotFoundError , jeśli plik nie
# istnieje

from pathlib import Path


# Pobierz od użytkownika nazwę pliku, np. abc.txt
plik = input("Podaj nazwę pliku: ") 

# Zmienna do zliczania wszystkich słów w pliku
suma = 0

try:  
    # Pobierz folder, w którym znajduje się uruchomiony program
    folder = Path(__file__).parent
    # Połącz folder programu z nazwą pliku podaną przez użytkownika
    sciezka = folder / plik
    # Otwórz plik do odczytu
    with open(sciezka, "r") as f: 
        # Przejdź po każdej linii pliku
        for linia in f:
            # Podziel linię na słowa i policz ich liczbę
            liczba_slow = len(linia.split())
            # Dodaj liczbę słów z tej linii do całkowitej sumy
            suma += liczba_slow
            print(liczba_slow)
# Jeśli plik nie istnieje, wyświetl komunikat o błędzie
except FileNotFoundError:
    print("Plik nie istnieje")
    