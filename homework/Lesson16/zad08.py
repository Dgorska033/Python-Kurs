# Symulacja Klient-Serwer: Stwórz prostą symulację interakcji Klient-Serwer przy użyciu
# klas.
# Napisz klasę FakeServer , która w __init__ tworzy "bazę danych" w postaci
# słownika, np. self.db = {"users": [{"id": 1, "name": "Jan"}, {"id": 2,
# "name": "Anna"}]} .
# Klasa FakeServer powinna mieć metodę handle_request(request: dict) , która
# analizuje żądanie (reprezentowane przez słownik).
# Jeśli metoda to GET a cel to /users , powinna zwrócić słownik-odpowiedź z
# kodem 200 i listą użytkowników w ciele.
# Jeśli metoda to POST a cel to /users , powinna dodać nowego użytkownika z
# ciała żądania do self.db i zwrócić odpowiedź z kodem 201 (Created).
# Dla każdego innego żądania, zwróć odpowiedź z kodem 404 (Not Found).
# Napisz klasę FakeClient z metodą send(server, request) , która "wysyła" żądanie
# do obiektu serwera i drukuje otrzymaną odpowiedź.
# Przetestuj scenariusze: pobranie wszystkich użytkowników, dodanie nowego
# użytkownika i próbę dostępu do nieistniejącego zasobu

class FakeServer:
    def __init__(self):
        # Prosta "baza danych" przechowywana w pamięci.
        self.db = {
            "users": [
                {"id": 1, "imie": "Jan"},
                {"id": 2, "imie": "Anna"}
            ]
        }

    def handle_request(self, request: dict):
        """Obsługuje żądanie klienta i zwraca odpowiedź."""

        metoda = request.get("method")
        cel = request.get("target")

        # GET /users -> zwracamy wszystkich użytkowników.
        if metoda == "GET" and cel == "/users":
            return {
                "status": 200,
                "body": self.db["users"]
            }

        # POST /users -> dodajemy nowego użytkownika.
        elif metoda == "POST" and cel == "/users":
            nowy_uzytkownik = request.get("body")

            self.db["users"].append(nowy_uzytkownik)

            return {
                "status": 201,
                "body": nowy_uzytkownik
            }

        # Każde inne żądanie -> 404 Not Found.
        else:
            return {
                "status": 404,
                "body": "Not Found"
            }


class FakeClient:
    def send(self, server, request):
        """Wysyła żądanie do serwera i wyświetla odpowiedź."""

        odpowiedz = server.handle_request(request)

        print("Żądanie:")
        print(request)

        print("Odpowiedź:")
        print(odpowiedz)

        print("--------------------")


# Tworzymy serwer i klienta.
serwer = FakeServer()
klient = FakeClient()


# 1. Pobranie wszystkich użytkowników.
pobierz_uzytkownikow = {
    "method": "GET",
    "target": "/users"
}

klient.send(serwer, pobierz_uzytkownikow)


# 2. Dodanie nowego użytkownika.
dodaj_uzytkownika = {
    "method": "POST",
    "target": "/users",
    "body": {
        "id": 3,
        "imie": "Kasia"
    }
}

klient.send(serwer, dodaj_uzytkownika)


# Sprawdzamy, czy nowy użytkownik został dodany.
klient.send(serwer, pobierz_uzytkownikow)


# 3. Próba dostępu do nieistniejącego zasobu.
nieistniejacy_zasob = {
    "method": "GET",
    "target": "/products"
}

klient.send(serwer, nieistniejacy_zasob)

