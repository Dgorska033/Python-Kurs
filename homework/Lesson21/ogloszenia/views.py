from django.shortcuts import render
from .models import Category


# Widok wyświetlający wszystkie kategorie
def category_list(request):
    # Pobieramy wszystkie kategorie z bazy danych
    categories = Category.objects.all()

    # Przekazujemy kategorie do szablonu
    return render(
        request,
        'ogloszenia/category_list.html',
        {'categories': categories}
    )

# Widok wyświetlający szczegóły jednej kategorii
def category_detail_view(request, pk):
    # Pobieramy jedną kategorię na podstawie jej ID
    category = Category.objects.get(pk=pk) #Pobierz jedną kategorię, której ID jest takie jak pk podane w adresie.

    return render(
        request,
        'ogloszenia/category_detail.html',
        {'category': category})