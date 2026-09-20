#  Klasa Request : Napisz klasę w Pythonie o nazwie HttpRequest .
# Konstruktor __init__ powinien przyjmować method , target oraz opcjonalnie
# headers (słownik) i body (string).
# Dodaj metodę display() , która będzie drukować sformatowane żądanie na konsoli w
# czytelnej formie, np.:
# --- HTTP Request ---
# Method: GET
# Target: /index.html
# Headers:
# Host: example.com
# User-Agent: PythonClient/1.0
# Body:
# (empty)
# --------------------
# Przetestuj klasę, tworząc obiekt dla żądania POST z przykładowymi danymi

class HttpRequest:
    def __init__(self, method, target, headers = None, body = None):
        self.method = method
        self.target = target 

        # Nagłówki są opcjonalne.
        # Jeśli ich nie podamy, zapisujemy pusty słownik.
        self.headers = headers if headers is not None else {}

        # Body również jest opcjonalne.
        self.body = body

    def display(self):
        """Wyświetla żądanie HTTP w czytelnej formie."""

        print("--- HTTP Request ---")

        print(f"Method: {self.method}")
        print(f"Target: {self.target}")

        print("Headers:")

        # Headers jest słownikiem.
        # Przechodzimy po jego kluczach i wartościach.
        for nazwa, wartosc in self.headers.items():
            print(f"{nazwa}: {wartosc}")

        print("Body:")

        # Jeśli body zawiera dane, wyświetlamy je.
        if self.body:
            print(self.body)
        else:
            print("(empty)")

        print("--------------------")


# Przykład 1 - podajemy wszystkie argumenty.
print("---- PRZYKŁAD 1 - wszystkie argumenty ----")
request_post = HttpRequest(
    method="POST",
    target="/api/articles",
    headers={
        "Host": "example.com",
        "User-Agent": "PythonClient/1.0"
    },
    body="Przykładowe dane")

request_post.display()


# Przykład 2 - nie podajemy opcjonalnych headers i body.
print("---- PRZYKŁAD 2 - bez opcjonalnych ----")
request_get = HttpRequest(
    method="GET",
    target="/index.html")

request_get.display()

