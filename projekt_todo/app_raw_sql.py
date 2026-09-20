# app_raw_sql.py
from database_raw import TaskManagerRaw


def pokaz_zadania(manager):
    """Wyświetla listę wszystkich zadań."""
    zadania = manager.pobierz_zadania()

    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")

    for zadanie in zadania:
        status = "✓" if zadanie[2] else "✗"

        print(
            f"[{status}] "
            f"ID: {zadanie[0]}, "
            f"Opis: {zadanie[1]}, "
            f"Priorytet: {zadanie[3]}")

def main():
    # Tworzymy obiekt klasy TaskManagerRaw.
    # Konstruktor __init__ automatycznie inicjalizuje bazę danych.
    manager = TaskManagerRaw()

    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie")
        print("6. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            pokaz_zadania(manager)

        elif wybor == "2":
            opis = input("Podaj opis zadania: ")

            try:
                priorytet = int(
                    input("Podaj priorytet zadania: ")
                )
                manager.dodaj_zadanie(opis, priorytet)
                print("Zadanie dodane!")
            except ValueError:
                print("Priorytet musi być liczbą.")

        elif wybor == "3":
            try:
                id_zadania = int(
                    input("Podaj ID zadania do oznaczenia: "))
                manager.oznacz_jako_zrobione(id_zadania)
                print("Zadanie zaktualizowane!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == "4":
            try:
                id_zadania = int(
                    input("Podaj ID zadania do usunięcia: "))
                manager.usun_zadanie(id_zadania)
                print("Zadanie usunięte!")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == "5":
            fraza = input("Podaj frazę do wyszukania: ")
            wyniki = manager.wyszukaj_zadania(fraza)

            if wyniki:
                print("\nZnalezione zadania:")

                for zadanie in wyniki:
                    # Rekord z Raw SQL jest krotką:
                    # zadanie[0] -> id
                    # zadanie[1] -> opis
                    # zadanie[2] -> zrobione
                    # zadanie[3] -> priorytet
                    status = "✓" if zadanie[2] else "✗"
                    print(
                        f"ID: {zadanie[0]}, "
                        f"Opis: {zadanie[1]}, "
                        f"Status: {status}, "
                        f"Priorytet: {zadanie[3]}")
            else:
                print(
                    "Nie znaleziono zadań zawierających tę frazę.")

        elif wybor == "6":
            print("Do zobaczenia!")
            break

        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()