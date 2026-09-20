# Walidator nagłówków: Napisz funkcję validate_request(request_dict: dict) ,
# która sprawdza, czy w słowniku reprezentującym żądanie HTTP znajdują się kluczowe
# nagłówki: Host i User-Agent .
# Jeśli któregoś z nagłówków brakuje w kluczu headers , funkcja powinna podnieść
# wyjątek ValueError z odpowiednim komunikatem (np. "Brak wymaganego nagłówka:
# Host").
# Użyj bloku try...except , aby przetestować działanie funkcji z poprawnym i
# niepoprawnym słownikiem żądania. To ćwiczenie łączy wiedzę o sieciach z obsługą
# wyjątków.

def validate_request(request_dict: dict):

    # Pobieramy słownik nagłówków z żądania.
    # Jeśli "headers" nie istnieje, dostaniemy pusty słownik {}.
    headers = request_dict.get("headers", {})

    # Sprawdzamy, czy istnieje wymagany nagłówek Host.
    if "Host" not in headers:
        raise ValueError("Brak wymaganego nagłówka: Host")

    # Sprawdzamy, czy istnieje wymagany nagłówek User-Agent.
    if "User-Agent" not in headers:
        raise ValueError("Brak wymaganego nagłówka: User-Agent")

    # Jeśli doszliśmy tutaj, oba nagłówki istnieją.
    return True


# ==================================================
print("PRZYKŁAD 1  POPRAWNE ŻĄDANIE \n")
# ==================================================

poprawne_zadanie = {
    "method": "GET",
    "target": "/users",
    "headers": {
        "Host": "example.com",
        "User-Agent": "PythonClient/1.0"
    }
}

try:
    validate_request(poprawne_zadanie)
    print("Żądanie jest poprawne.")

except ValueError as blad:
    print(f"Błąd: {blad}")


# ==================================================
print("\n PRZYKŁAD 2  NIEPOPRAWNE ŻĄDANIE \n")
# ==================================================

# Tutaj celowo nie podajemy nagłówka Host,
# żeby sprawdzić działanie wyjątku.

niepoprawne_zadanie = {
    "method": "GET",
    "target": "/users",
    "headers": {
        "User-Agent": "PythonClient/1.0"
    }
}

try:
    validate_request(niepoprawne_zadanie)
    print("Żądanie jest poprawne.")

except ValueError as blad:
    print(f"Błąd: {blad}")