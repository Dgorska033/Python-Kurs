from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


# Widok strony z informacjami
def info(request):
    return HttpResponse("Informacje o stronie")


# Widok regulaminu
def rules(request):
    return HttpResponse("Regulamin")

# Dynamiczny widok profilu użytkownika
# username zostanie pobrany z adresu URL
def user_profile(request, username):
    return HttpResponse(f"Witaj na profilu, {username}!")


# Widok pobierający wszystkie produkty z bazy
def product_list(request):
    products = Product.objects.all()

    return render(
        request,
        'ogloszenia/product_list.html',
        {'products': products}
    )

# Widok odpowiedzialny za dodawanie nowego produktu
def product_create(request):

    # POST - użytkownik wysłał wypełniony formularz
    if request.method == 'POST':
        form = ProductForm(request.POST)

        # Sprawdzamy, czy dane są poprawne
        if form.is_valid():
            # Zapisujemy nowy produkt do bazy danych
            form.save()

            # Po zapisaniu przekierowujemy na listę produktów
            return redirect('product_list')

    # GET - użytkownik dopiero wszedł na stronę
    else:
        # Tworzymy pusty formularz
        form = ProductForm()

    # Wyświetlamy formularz w szablonie
    return render(
        request,
        'ogloszenia/product_form.html',
        {'form': form}
    )

# Widok wyświetlający produkty należące do wybranej kategorii
def products_by_category(request, category_id):

    # Pobieramy tylko produkty, których category_id
    # jest takie samo jak ID przekazane w adresie URL
    products = Product.objects.filter(category_id=category_id) #linijka klucz
    

    return render(
        request,
        'ogloszenia/products_by_category.html',
        {'products': products}
    )