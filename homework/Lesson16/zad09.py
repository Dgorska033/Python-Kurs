# PUT vs PATCH: Wyobraź sobie, że na serwerze pod adresem /users/1 znajduje się
# następujący zasób w formacie JSON: {"name": "Katarzyna", "email":
# "k.nowak@example.com", "city": "Warszawa"} .
# Opisz, jak wyglądałoby ciało żądania PUT , aby zmienić tylko imię na "Kasia".
# Opisz, jak wyglądałoby ciało żądania PATCH , aby zmienić tylko imię na "Kasia".
# Wyjaśnij w komentarzu w kodzie, dlaczego te żądania się różnią i która metoda jest
# bardziej "oszczędna" pod względem przesyłanych danych

# Na serwerze pod adresem /users/1 znajduje się użytkownik:
# {"name": "Katarzyna", "email": "k.nowak@example.com", "city": "Warszawa"}
#
# PUT ma zastąpić cały zasób nową wersją.
# PATCH ma zmienić tylko wskazane dane.


class FakeServer:

    def __init__(self):
        # Udajemy bazę danych.
        # Mamy jednego użytkownika o ID = 1.
        self.db = {
            "users": {
                "1": {
                    "name": "Katarzyna",
                    "email": "k.nowak@example.com",
                    "city": "Warszawa"
                }
            }
        }

    def handle_request(self, request: dict, id):
        # Zamieniamy ID na tekst, ponieważ klucz "1"
        # w naszej bazie danych jest stringiem.
        user_key = str(id)

        # ---------------------------------------
        # PUT
        # ---------------------------------------

        if request["method"] == "PUT" and request["target"] == "/users":

            # Sprawdzamy, czy użytkownik istnieje.
            if user_key in self.db["users"]:

                # PUT zastępuje CAŁY zapis użytkownika
                # nowymi danymi przesłanymi w body.
                self.db["users"][user_key] = request["body"]

                return {
                    "code": 200,
                    "body": "Replaced",
                    "comment": self.db["users"]
                }

            # Jeżeli użytkownika nie ma, zwracamy 404.
            return {
                "code": 404,
                "body": "User not found"
            }

        # ---------------------------------------
        # PATCH
        # ---------------------------------------

        elif request["method"] == "PATCH" and request["target"] == "/users":

            # Sprawdzamy, czy użytkownik istnieje.
            if user_key in self.db["users"]:

                # PATCH aktualizuje tylko pola,
                # które zostały przesłane w body.
                #
                # update() nie usuwa pozostałych danych.
                self.db["users"][user_key].update(request["body"])

                return {
                    "code": 200,
                    "body": "Updated",
                    "comment": self.db["users"]
                }

            return {
                "code": 404,
                "body": "User not found"
            }

        # Jeżeli metoda lub adres są inne niż obsługiwane.
        return {
            "code": 404,
            "body": "Not Found"
        }


# Tworzymy nasz fałszywy serwer.
serwer = FakeServer()


# ==================================================
# PRZYKŁAD 1 – PUT
# ==================================================

# Chcemy zmienić imię Katarzyna -> Kasia.
#
# Przy PUT wysyłamy CAŁY zasób ponownie,
# również pola, których nie zmieniamy.

put_request = {
    "method": "PUT",
    "target": "/users",
    "body": {
        "name": "Kasia",
        "email": "k.nowak@example.com",
        "city": "Warszawa"
    }
}

print("----- PUT -----")

odpowiedz_put = serwer.handle_request(put_request, 1)

print(odpowiedz_put)


# ==================================================
# PRZYKŁAD 2 – PATCH
# ==================================================

# Przy PATCH wysyłamy tylko pole,
# które chcemy zmienić.
#
# Nie musimy ponownie przesyłać emaila i miasta.

patch_request = {
    "method": "PATCH",
    "target": "/users",
    "body": {
        "name": "Kasia"
    }
}

print("\n----- PATCH -----")

odpowiedz_patch = serwer.handle_request(patch_request, 1)

print(odpowiedz_patch)


# ==================================================
# RÓŻNICA PUT vs PATCH
# ==================================================

# PUT:
# zastępuje cały zasób nową wersją.
# Dlatego jeśli chcemy zmienić tylko imię,
# nadal przesyłamy name, email i city.
#
# PATCH:
# zmienia tylko wskazane pola.
# Jeśli chcemy zmienić tylko imię,
# wystarczy przesłać:
#
# {"name": "Kasia"}
#
# PATCH jest w tym przypadku bardziej oszczędny,
# ponieważ przesyłamy mniej danych.