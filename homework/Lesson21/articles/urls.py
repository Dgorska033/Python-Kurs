from django.urls import path
from .views import article_list_view


urlpatterns = [
    path('', article_list_view, name='article-list'),
]