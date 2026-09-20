# Lekcja 22 
sprawozdanie z wykonania zadań

_---------------------------------
## Zadanie 1 – Kategorie i relacja ForeignKey
_---------------------------------

Utworzono model Category z polem name oraz model Post. Każdy post został powiązany z jedną kategorią przy użyciu ForeignKey.

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

Pole:

category = models.ForeignKey(Category, on_delete=models.CASCADE)

tworzy relację wiele-do-jednego: wiele postów może należeć do jednej kategorii, natomiast pojedynczy post wskazuje jedną kategorię.

on_delete=models.CASCADE oznacza, że usunięcie kategorii powoduje również usunięcie powiązanych z nią postów.

publication_date korzysta z:

auto_now_add=True

dzięki czemu data i godzina utworzenia posta są zapisywane automatycznie.

Po utworzeniu modeli wykonano migracje:

python manage.py makemigrations
python manage.py migrate

makemigrations tworzy pliki opisujące zmiany struktury modeli, natomiast migrate stosuje te zmiany w bazie danych.

Rezultat: utworzono znormalizowaną strukturę, w której nazwa kategorii nie musi być powtarzana jako tekst w każdym poście.

_---------------------------------
## Zadanie 2 – Widok kategorii
_---------------------------------

Utworzono widok wyświetlający wszystkie posty należące do wskazanej kategorii.

def category_posts(request, category_id):
    category = Category.objects.get(id=category_id)

    posts = Post.objects.filter(category=category)

    return render(
        request,
        'blog/category_posts.html',
        {
            'category': category,
            'posts': posts
        }
    )

Do aplikacji dodano dynamiczny URL:

path(
    'category/<int:category_id>/',
    views.category_posts,
    name='category_posts'
)

Przykładowy adres:

/category/5/

przekazuje do widoku:

category_id = 5

Następnie:

Category.objects.get(id=category_id)

pobiera pojedynczą kategorię, a:

Post.objects.filter(category=category)

zwraca QuerySet wszystkich postów należących do tej kategorii.

get() a filter()

Category.objects.get(id=1)

get() służy do pobrania jednego konkretnego obiektu.

Post.objects.filter(category=category)

filter() zwraca zbiór obiektów spełniających podany warunek.

Rezultat: adres /category/<category_id>/ wyświetla posty należące tylko do wskazanej kategorii.

_---------------------------------

## Zadanie 3 – Pięć najnowszych postów

_---------------------------------


Utworzono widok strony głównej wyświetlający maksymalnie pięć najnowszych postów.

def home(request):
    posts = Post.objects.order_by('-publication_date')[:5]

    return render(
        request,
        'blog/home.html',
        {'posts': posts}
    )

Najważniejsza operacja:

Post.objects.order_by('-publication_date')[:5]

składa się z dwóch elementów.

Sortowanie

.order_by('-publication_date')

sortuje posty według daty publikacji od najnowszego do najstarszego. Minus przed nazwą pola oznacza kolejność malejącą.

Slicing

[:5]

ogranicza QuerySet do pierwszych pięciu wyników.

Slicing nie jest paginacją – pozostałe rekordy nie są wyświetlane na kolejnej stronie, lecz zostają pominięte przez to zapytanie.

Test: po utworzeniu większej liczby postów strona główna nadal wyświetlała dokładnie pięć najnowszych rekordów.

Zadanie 4 – Instalacja biblioteki Faker

Bibliotekę Faker zainstalowano w wirtualnym środowisku projektu:

pip install Faker

Poprawność instalacji można sprawdzić poleceniem:

pip show Faker

Pakiet został zainstalowany w .venv należącym do projektu Lekcji 22.

Znaczenie środowiska wirtualnego

Każde środowisko .venv posiada własny zestaw zainstalowanych pakietów. Uruchomienie skryptu interpreterem z innego projektu może powodować np.:

ModuleNotFoundError: No module named 'faker'

Dlatego przed pracą z projektem należy aktywować jego środowisko:

cd "D:\Python Kurs\homework\Lesson22"
.\.venv\Scripts\Activate.ps1


_---------------------------------
# Zadanie 5 – Testowanie Fakera
_---------------------------------


Utworzono samodzielny plik:

faker_test.py

umieszczony poza aplikacją blog.

Skrypt:

from faker import Faker


fake = Faker('pl_PL')


print("=== LOSOWE IMIONA I NAZWISKA ===")

for i in range(10):
    print(fake.name())


print("\n=== LOSOWE ZDANIA ===")

for i in range(10):
    print(fake.sentence())

Uruchomienie:

python faker_test.py

Faker('pl_PL') ustawia polską lokalizację generatora.

Przykładowe metody biblioteki:

fake.name()
fake.sentence()
fake.text()

Rezultat: skrypt generuje 10 losowych polskich imion i nazwisk oraz 10 losowych zdań.

Faker został później wykorzystany do automatycznego generowania danych testowych w bazie.



_---------------------------------
# Zadanie 6 – Wyszukiwarka postów
_---------------------------------


Na stronie głównej dodano formularz wykorzystujący metodę GET:

<form method="GET" action="{% url 'search_posts' %}">
    <input
        type="text"
        name="q"
        placeholder="Wpisz szukaną frazę"
    >

    <button type="submit">Szukaj</button>
</form>

Dla frazy Python adres może mieć postać:

/search/?q=Python

Wartość parametru jest pobierana w widoku:

query = request.GET.get('q', '')

Do obsługi warunku „tytuł LUB treść” wykorzystano obiekt Q:

from django.db.models import Q

Zapytanie:

posts = Post.objects.filter(
    Q(title__icontains=query) |
    Q(content__icontains=query)
)

Operator:

|

oznacza logiczne LUB.

Lookup:

__icontains

sprawdza, czy pole zawiera podany fragment tekstu bez uwzględniania wielkości liter.

Przykładowo wyszukanie:

python

może znaleźć:

Python dla początkujących

Rezultat: wyszukiwarka znajduje post, jeżeli podana fraza znajduje się w jego tytule lub treści.


_---------------------------------
#  Zadanie 7 – Seeder kategorii i postów
_---------------------------------


Utworzono własną komendę Django:

python manage.py seed_blog

Struktura plików:

blog/
└── management/
    ├── __init__.py
    └── commands/
        ├── __init__.py
        └── seed_blog.py

Django wykrywa własne komendy znajdujące się w:

<aplikacja>/management/commands/

Podstawą komendy jest:

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        ...

Kod umieszczony w handle() jest wykonywany po uruchomieniu:

python manage.py seed_blog

Czyszczenie danych

Seeder usuwa istniejące posty i kategorie:

Post.objects.all().delete()
Category.objects.all().delete()

Predefiniowane kategorie

Utworzono listę kategorii:

category_names = [
    'Technologia',
    'Podróże',
    'Kulinaria',
    'Sport',
    'Muzyka',
    'Filmy',
    'Nauka'
]

Następnie obiekty są tworzone w bazie:

categories = []

for name in category_names:
    category = Category.objects.create(name=name)
    categories.append(category)

Generowanie 100 postów

for i in range(100):
    Post.objects.create(
        title=fake.sentence(nb_words=6),
        content=fake.text(),
        category=random.choice(categories)
    )

range(100) powoduje wykonanie kodu 100 razy.

random.choice(categories) wybiera losową kategorię dla każdego tworzonego posta.

Faker generuje tytuł oraz treść.

Rezultat: jedno uruchomienie seed_blog usuwa wcześniejsze dane, tworzy 7 kategorii i 100 nowych postów przypisanych losowo do kategorii.


_---------------------------------
# Zadanie 8 – Normalizacja postów za pomocą tagów
_---------------------------------


Dodano model:

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

Model Post rozszerzono o:

tags = models.ManyToManyField(
    Tag,
    blank=True
)

ManyToManyField realizuje relację wiele-do-wielu:

jeden post może mieć wiele tagów,

jeden tag może być przypisany do wielu postów.

Przykładowe relacje:

Post 1 ─── Python
   │          │
   ├── Django │
   │          │
Post 2 ───────┘

Django tworzy dla ManyToManyField tabelę pośrednią przechowującą identyfikatory powiązanych rekordów, np.:

post_id | tag_id
--------|-------
1       | 2
1       | 5
2       | 2

blank=True pozwala utworzyć post bez przypisanych tagów.

Po zmianie modeli wykonano:

python manage.py makemigrations
python manage.py migrate

Rezultat: tag nie musi być zapisywany wielokrotnie jako tekst w każdym poście. Istnieje jako osobny rekord, a baza przechowuje relacje między postami i tagami.


_---------------------------------
# Zadanie 9 – Rozbudowa seedera o tagi
_---------------------------------


Komendę seed_blog rozszerzono o tworzenie tagów i przypisywanie ich do postów.

Przykładowa lista:

tag_names = [
    'Python',
    'Django',
    'AI',
    'Programowanie',
    'Zdrowie',
    'Lifestyle',
    'Porady',
    'Recenzje',
    'Europa',
    'Hobby'
]

Tworzenie obiektów:

tags = []

for name in tag_names:
    tag = Tag.objects.create(name=name)
    tags.append(tag)

Dla każdego posta losowana jest liczba tagów od 1 do 5:

random_tags = random.sample(
    tags,
    k=random.randint(1, 5)
)

random.randint(1, 5) losuje liczbę tagów.

random.sample() wybiera wskazaną liczbę różnych elementów z listy.

Powiązania są zapisywane za pomocą:

post.tags.set(random_tags)

W przypadku ManyToManyField nie przypisuje się listy bezpośrednio:

post.tags = random_tags

Relacją zarządza Django poprzez menedżer pola wiele-do-wielu i tabelę pośrednią.

Przypisane tagi można sprawdzić przez:

post.tags.all()

oraz policzyć:

post.tags.count()

Rezultat: każdy ze 100 wygenerowanych postów otrzymuje od 1 do 5 losowo wybranych tagów.


_---------------------------------
# Zadanie 10 – Rejestracja i logowanie przez django-allauth
_---------------------------------


Do projektu zintegrowano zewnętrzną aplikację django-allauth.

Instalacja:

pip install django-allauth

Konfiguracja aplikacji

Do INSTALLED_APPS dodano:

'allauth',
'allauth.account',

Dodano wymagany middleware:

'allauth.account.middleware.AccountMiddleware',

Skonfigurowano backend uwierzytelniania:

AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
]

Routing

W głównym pliku:

mojastrona/urls.py

dodano:

path('accounts/', include('allauth.urls')),

Dzięki temu aplikacja udostępnia gotowe adresy, m.in.:

/accounts/signup/
/accounts/login/
/accounts/logout/

Po instalacji wykonano migracje:

python manage.py migrate

Przekierowania

W settings.py skonfigurowano:

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

Po zalogowaniu użytkownik wraca na stronę główną. Po wylogowaniu również następuje przekierowanie na /.

Informacja o stanie logowania

Na stronie głównej dodano sprawdzenie:

{% if user.is_authenticated %}

    <p>
        Zalogowana jako: <strong>{{ user.username }}</strong>
    </p>

{% else %}

    <p>Nie jesteś zalogowana.</p>

{% endif %}

user.is_authenticated pozwala sprawdzić, czy bieżące żądanie pochodzi od zalogowanego użytkownika.

Test funkcjonalny

Sprawdzono następujący przepływ:

rejestracja
    ↓
zalogowany użytkownik
    ↓
wylogowanie
    ↓
ponowne logowanie

Po rejestracji aplikacja prawidłowo rozpoznawała zalogowanego użytkownika. Widok wylogowania django-allauth wyświetlał stronę potwierdzającą operację Sign Out.

Rezultat: projekt obsługuje rejestrację, logowanie oraz wylogowanie użytkowników za pomocą zewnętrznej aplikacji.