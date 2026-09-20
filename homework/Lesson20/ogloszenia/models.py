from django.db import models


# Model kategorii produktu
class Category(models.Model):

    # Nazwa kategorii, np. "Elektronika"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model reprezentujący produkt
class Product(models.Model):

    # Nazwa produktu - maksymalnie 100 znaków
    name = models.CharField(max_length=100)

    # Dłuższy opis produktu
    description = models.TextField()

    # Cena produktu - maksymalnie 6 cyfr łącznie,
    # w tym 2 cyfry po przecinku
    # Maksymalna wartość: 9999.99
    price = models.DecimalField(max_digits=6, decimal_places=2)



     # Kategoria, do której należy produkt
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True    # null = True bo mam już produkty w bazie
    )

    # Wyświetla nazwę produktu zamiast "Product object (1)"
    def __str__(self):
        return self.name