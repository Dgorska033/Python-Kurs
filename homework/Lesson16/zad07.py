# Parser URL: Napisz funkcję parse_url(url: str) -> dict , która przyjmuje jako
# argument adres URL w formie stringa (np.
# https://api.example.com:8080/users/search?active=true ) i zwraca słownik
# zawierający jego części: protocol , domain , port i path .
# Dla podanego przykładu, wynik powinien być: {'protocol': 'https', 'domain':
# 'api.example.com', 'port': 8080, 'path': '/users/search?active=true'} .
# Obsłuż przypadek, gdy port nie jest podany (dla http domyślny to 80, dla https 443).
# Wskazówka: Użyj metod do manipulacji stringami, takich jak split() czy find() .

def parse_url(url: str) -> dict:

    # Oddzielamy protokół od pozostałej części adresu.
    protocol, reszta = url.split("://", 1)

    # Oddzielamy adres serwera od ścieżki.
    host, path = reszta.split("/", 1)
    path = "/" + path

    # Jeśli w adresie serwera znajduje się ":",
    # oznacza to, że port został podany.
    if ":" in host:
        domain, port = host.split(":", 1)
        port = int(port)

    # Jeśli port nie został podany,
    # ustawiamy domyślny port zależnie od protokołu.
    else:
        domain = host

        if protocol == "http":
            port = 80
        elif protocol == "https":
            port = 443

    # Zwracamy wszystkie części URL jako słownik.
    return {
        "protocol": protocol,
        "domain": domain,
        "port": port,
        "path": path
    }


url = "https://api.example.com:8080/users/search?active=true"

print(parse_url(url))

print(parse_url("http://blacla.com/test"))
print(parse_url("https://xdddddd.com/test"))  

print(parse_url("https://facebook.com/"))