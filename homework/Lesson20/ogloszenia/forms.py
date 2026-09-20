from django import forms
from .models import Product


# Formularz do dodawania nowych produktów
class ProductForm(forms.ModelForm):

    class Meta:
        # Formularz korzysta z modelu Product
        model = Product

        # Pola dostępne w formularzu
        fields = ['name', 'description', 'price']