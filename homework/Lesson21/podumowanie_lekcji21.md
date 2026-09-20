Lekcja 21 --podsumowanie
Struktura projektu

Projekt: D:\Python Kurs\homework\Lesson21

Aplikacje: - ogloszenia -- kategorie - articles -- artykuły -
mojastrona -- konfiguracja projektu

W INSTALLED_APPS dodano ogloszenia oraz articles.

Zadanie 1 -- model Category

W ogloszenia/models.py utworzono:

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

Następnie:

python manage.py makemigrations
python manage.py migrate

CharField przechowuje nazwę, a __str__() określa czytelną
reprezentację obiektu.

Zadanie 2 -- dodawanie danych w shellu

python manage.py shell

from ogloszenia.models import Category

Category.objects.create(name="Sport")
Category.objects.create(name="Technologia")
Category.objects.create(name="Kultura")
Category.objects.all()

objects.create() tworzy i zapisuje rekord w bazie.

Zadanie 3 -- lista kategorii

W ogloszenia/views.py:

from django.shortcuts import render
from .models import Category

def category_list(request):
    categories = Category.objects.all()
    return render(
        request,
        'ogloszenia/category_list.html',
        {'categories': categories}
    )

W ogloszenia/urls.py:

from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list, name='category_list'),
]

W category_list.html:

<h1>Lista kategorii</h1>

<ul>
    {% for category in categories %}
        <li>{{ category.name }}</li>
    {% endfor %}
</ul>

Widok działa pod /categories/.

Zadanie 4 -- pliki statyczne CSS

Utworzono:

ogloszenia/static/ogloszenia/style.css

body {
    background-color: #f0f8ff;
}

W szablonie:

{% load static %}
<link rel="stylesheet" href="{% static 'ogloszenia/style.css' %}">

Folder ogloszenia wewnątrz static działa jako namespace i zapobiega
konfliktom nazw.

Zadanie 5 -- get()

W shellu:

from ogloszenia.models import Category
Category.objects.get(name="Sport")

get() zwraca jeden konkretny obiekt. filter() zwraca QuerySet.

Zadanie 6 -- szczegóły kategorii

W ogloszenia/views.py:

def category_detail_view(request, pk):
    category = Category.objects.get(pk=pk)

    return render(
        request,
        'ogloszenia/category_detail.html',
        {'category': category}
    )

Routing:

path(
    'categories/<int:pk>/',
    views.category_detail_view,
    name='category_detail'
),

Szablon:

<h1>{{ category.name }}</h1>

<int:pk> pobiera liczbę z URL i przekazuje ją do widoku jako pk
(primary key).

Zadanie 7 -- relacja Category i Article

Utworzono aplikację:

python manage.py startapp articles

Model Article:

from django.db import models
from ogloszenia.models import Category

class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title

Po zmianach wykonano migracje.

W shellu utworzono przykładowe artykuły i przypisano je do kategorii,
m.in.:

from articles.models import Article
from ogloszenia.models import Category
from django.utils import timezone

sport = Category.objects.get(name="Sport")
technologia = Category.objects.get(name="Technologia")
kultura = Category.objects.get(name="Kultura")

Article.objects.create(
    title="Mecz reprezentacji Polski",
    pub_date=timezone.now(),
    category=sport
)

Article.objects.create(
    title="Nowości w Pythonie",
    pub_date=timezone.now(),
    category=technologia
)

Article.objects.create(
    title="Sztuczna inteligencja",
    pub_date=timezone.now(),
    category=technologia
)

Article.objects.create(
    title="Nowa wystawa w muzeum",
    pub_date=timezone.now(),
    category=kultura
)

Relację odwrotną sprawdzono przez:

technologia.article_set.all()

W category_detail.html:

<ul>
    {% for article in category.article_set.all %}
        <li>{{ article.title }}</li>
    {% empty %}
        <li>Brak artykułów w tej kategorii.</li>
    {% endfor %}
</ul>

ForeignKey tworzy relację wiele-do-jednego. Jedna kategoria może mieć
wiele artykułów. Django automatycznie udostępnia relację odwrotną
article_set.

Zadanie 8 -- is_published i NOWOŚĆ!

Do modelu Article dodano:

is_published = models.BooleanField(default=True)

Po zmianie wykonano makemigrations i migrate.

Lista pobiera tylko opublikowane artykuły:

Article.objects.filter(
    is_published=True
).order_by('-pub_date')

Datę sprzed 3 dni wyliczono:

from datetime import timedelta
from django.utils import timezone

three_days_ago = timezone.now() - timedelta(days=3)

W szablonie:

{% if article.pub_date >= three_days_ago %}
    <span>NOWOŚĆ!</span>
{% endif %}

Artykuł z is_published=False nie pojawia się na liście.

Zadanie 9 -- zmiana panelu administratora

Utworzono:

templates/admin/base_site.html

W mojastrona/settings.py ustawiono:

'DIRS': [BASE_DIR / 'templates'],

W base_site.html:

{% extends "admin/base_site.html" %}

{% block branding %}
<div id="site-name">
    <a href="{% url 'admin:index' %}">
        Panel Administratora Mojej Strony
    </a>
</div>
{% endblock %}

W /admin/ napis Django administration został zastąpiony przez
Panel Administratora Mojej Strony.

Lesson21 ma własną bazę db.sqlite3, dlatego utworzono również osobnego
superusera.

Zadanie 10 -- wyszukiwarka artykułów

W article_list.html dodano formularz GET:

<form method="GET">
    <input
        type="text"
        name="q"
        placeholder="Szukaj artykułu..."
        value="{{ query|default:'' }}"
    >

    <button type="submit">Szukaj</button>
</form>

W article_list_view:

query = request.GET.get('q')

if query:
    articles = articles.filter(
        title__icontains=query
    )

Do kontekstu przekazano także:

'query': query,

Przykład:

/articles/?q=Python

request.GET.get('q') pobiera parametr q z query string.
title__icontains wyszukuje frazę w tytule bez rozróżniania wielkości
liter.

Najważniejsze rzeczy z Lekcji 21

ORM

Category.objects.all()
Category.objects.get(name="Sport")
Article.objects.filter(is_published=True)
articles.filter(title__icontains=query)

ForeignKey

category = models.ForeignKey(
    Category,
    on_delete=models.CASCADE,
    null=True
)

Relacja odwrotna:

category.article_set.all()

Dynamiczny URL

path('categories/<int:pk>/', ...)

Dane przekazywane do template

return render(
    request,
    'template.html',
    {'category': category}
)

Pętla w template

{% for article in articles %}
    {{ article.title }}
{% empty %}
    Brak artykułów
{% endfor %}

Warunek w template

{% if article.pub_date >= three_days_ago %}
    NOWOŚĆ!
{% endif %}

Parametr GET

query = request.GET.get('q')

Static

{% load static %}
{% static 'ogloszenia/style.css' %}

Override admina

templates/admin/base_site.html

