from django.db import models


# Model reprezentujący kategorię
class Category(models.Model):
    # Nazwa kategorii, maksymalnie 100 znaków
    name = models.CharField(max_length=100)

    # Określa, jak kategoria będzie wyświetlana np. w panelu admina
    def __str__(self):
        return self.name