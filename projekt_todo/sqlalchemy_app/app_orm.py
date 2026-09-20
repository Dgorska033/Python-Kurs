from . import database as db

def pokaz_zadania():
    """Wyświetla ID, opis i status wszystkich zadań."""

    zadania = db.pobierz_zadania()

    if not zadania:
        print("Brak zadań na liście.")
        return

    print("\n--- Twoja lista zadań ---")

    for zadanie in zadania:

        # Jeśli zrobione = True wyświetlamy ✓,
        # jeśli False wyświetlamy x.
        status = "✓" if zadanie.zrobione else "x"

        # W ORM zadanie jest obiektem klasy Zadanie,
        # dlatego ID odczytujemy przez zadanie.id.
        print(
            f"[{status}] ID: {zadanie.id}, "
            f"Opis: {zadanie.opis}"
        )


def main():
    # Tworzy tabelę, jeśli jeszcze nie istnieje.
    db.init_db()

    while True:
        print("Menu:")
        print("1. Pokaż zadania")
        print("2. Dodaj zadanie")
        print("3. Oznacz zadanie jako zrobione")
        print("4. Usuń zadanie")
        print("5. Wyszukaj zadanie")
        print("6. Dodaj tag do zadania")
        print("7. Edytuj zadanie")
        print("8. Wyjdź")

        wybor = input("Wybierz opcję: ")

        # POKAŻ ZADANIA
        if wybor == "1":
            pokaz_zadania()

        # DODAJ ZADANIE
        elif wybor == "2":
            opis = input("Podaj opis zadania: ")

            # Przekazujemy opis do funkcji w database.py.
            db.dodaj_zadanie(opis)

            print("Zadanie dodane!")

        # OZNACZ ZADANIE JAKO ZROBIONE
        elif wybor == "3":
            try:
                id_zadania = int(
                    input("Podaj ID zadania do oznaczenia: ")
                )

                # Przekazujemy ID zadania do warstwy danych.
                if db.oznacz_jako_zrobione(id_zadania):
                    print("Zadanie zaktualizowane!")
                else:
                    print("Zadanie o takim ID nie istnieje.")

            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        # USUŃ ZADANIE
        elif wybor == "4":
            try:
                id_zadania = int(
                    input("Podaj ID zadania do usunięcia: ")
                )
                # Funkcja znajduje obiekt Zadanie o podanym ID,
                # a następnie usuwa go za pomocą db.delete()
                # i zatwierdza zmianę przez db.commit().
                if db.usun_zadanie(id_zadania):
                    print("Zadanie usunięte!")
                else:
                    print("Zadanie o takim ID nie istnieje.")

            except ValueError:
                print("Błędne ID. Podaj liczbę.")

        elif wybor == "5":
            # Pobieramy od użytkownika fragment opisu.
            fraza = input("Podaj frazę do wyszukania: ")

            # Funkcja ORM zwraca listę obiektów klasy Zadanie.
            wyniki = db.wyszukaj_zadania(fraza)

            if wyniki:
                print("\nZnalezione zadania:")

                for zadanie in wyniki:
            # W ORM nie używamy indeksów zadanie[0], zadanie[1] itd.
            # Każdy wynik jest obiektem klasy Zadanie,
            # dlatego korzystamy z jego atrybutów.
                    status = "✓" if zadanie.zrobione else "X"

                print(
                    f"ID: {zadanie.id}, "
                    f"Opis: {zadanie.opis}, "
                    f"Status: {status}")
            else:
                print("Nie znaleziono zadań zawierających tę frazę.")

        elif wybor == "6":
            try:
                id_zadania = int(
                    input("Podaj ID zadania: "))
                nazwa_tagu =( 
                    input("Podaj nazwę taga: "))

                if db.dodaj_tag_do_zadania(id_zadania, nazwa_tagu):
                    print("Tag został dodany do zadania.")
                else:
                    print("Zadanie o takim ID nie istnieje.")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == "7":
            try:
                id_zadania = int(input("Podaj ID zadania do edycji: "))

                nowy_opis = input("Podaj nowy opis zadania: ")

                if db.edytuj_zadanie(id_zadania, nowy_opis):
                    print("Opis zadania został zmieniony!")
                else:
                    print("Zadanie o takim ID nie istnieje.")
            except ValueError:
                print("Błędne ID. Podaj liczbę.")
        elif wybor == "8":
            print("Do zobaczenia!")
            break
        else:
            print("Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main()
    