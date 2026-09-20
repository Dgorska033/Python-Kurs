from django.urls import path
from . import views


urlpatterns = [
    # Statyczna trasa do strony informacyjnej
    path('info/', views.info, name='info'),

    # Statyczna trasa do regulaminu
    path('rules/', views.rules, name='rules'),


    # Dynamiczna trasa - username może być różnym tekstem
    path('user/<str:username>/', views.user_profile, name='user_profile'),


     # Lista produktów
    path('products/', views.product_list, name='product_list'),

    # Trasa do formularza dodawania produktu
    path('products/add/', views.product_create, name='product_create'),

    # Dynamiczna trasa - produkty należące do konkretnej kategorii
path(
    'category/<int:category_id>/',   # Weź liczbę znajdującą się w tym miejscu URL i przekaż ją do widoku jako category_id.
    views.products_by_category,
    name='products_by_category'
),
]


