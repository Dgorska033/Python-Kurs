from django.db import models


# Model reprezentujący pojedyncze ogłoszenie w bazie danych
class Ogloszenie(models.Model):

    # Tytuł ogłoszenia - maksymalnie 100 znaków
    tytul = models.CharField(max_length=100)

    # Opis ogłoszenia - może zawierać dłuższy tekst
    opis = models.TextField()

    # Cena - maksymalnie 8 cyfr łącznie, w tym 2 cyfry po przecinku
    # Przykładowa maksymalna wartość: 999999.99
    cena = models.DecimalField(max_digits=8, decimal_places=2)

    # Data i godzina zostaną ustawione automatycznie
    # podczas pierwszego utworzenia ogłoszenia
    data_dodania = models.DateTimeField(auto_now_add=True)

    # Określa, jak obiekt będzie wyświetlany np. w panelu admina
    # Zamiast "Ogloszenie object (1)" wyświetli tytuł ogłoszenia
    def __str__(self):
        return self.tytul