from django.urls import path
from . import views


urlpatterns = [

    # Strona główna - Zadanie 3
    path('', views.home, name='home'),

    # Posty należące do wybranej kategorii - Zadanie 2
    path(
        'category/<int:category_id>/',
        views.category_posts,
        name='category_posts'
    ),

    path('search/', views.search_posts, name='search_posts'),
]