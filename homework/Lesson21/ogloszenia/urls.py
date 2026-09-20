from django.urls import path
from . import views


urlpatterns = [
    # Lista wszystkich kategorii
    path('categories/', views.category_list, name='category_list'),

    # Szczegóły konkretnej kategorii
    path(
    'categories/<int:pk>/',
    views.category_detail_view,
    name='category_detail'
),
]