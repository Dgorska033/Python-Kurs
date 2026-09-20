# Model żądania: Utwórz w Pythonie słownik, który będzie reprezentował żądanie GET w
# celu pobrania listy wszystkich artykułów z adresu /api/articles . W nagłówkach dodaj
# klucz Host z wartością my-blog.com 

zadanie_get = {

    "method": "GET",             # metoda HTTP  GET> co chcemy zrobic
    "target": "/api/articles",   # endpoint, do którego wysyłamy żądanie  API/ARTICLES > gdzie
    "version": "HTTP/1.1",
    "headers": {                 # nagłówki HTTP
        "Host": "my-blog.com"    # serwer, do którego kierowane jest żądanie > my.blog.com > do jakiego hosta
    },
    "body": None
}

print(zadanie_get)

# Headers jest kolejnym słownikiem (zagniżdzenie) , bo request moze miec wiele nagłówkow

