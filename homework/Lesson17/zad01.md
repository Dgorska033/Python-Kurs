# Zadanie 1 – Strona "O mnie"
# Stwórz nową ścieżkę /me w swojej aplikacji. Kiedy użytkownik wejdzie na ten adres, funkcja
# powinna zwrócić Twoje imię i nazwisko.

Dodałam do aplikacji Flask nową ścieżkę /me.
Użyłam dekoratora @app.route('/me'), który określa,
jaka funkcja ma zostać uruchomiona po wejściu na adres /me.

Utworzyłam funkcję me(), która zwraca moje imię i nazwisko
za pomocą return.

Po uruchomieniu aplikacji:
http://127.0.0.1:5000/    -> otwiera stronę główną
http://127.0.0.1:5000/me  -> uruchamia funkcję me()
                             i wyświetla moje imię i nazwisko.

Kod dodany do app1.py:

@app.route('/me')
def me():
    return 'Dominika Górska'