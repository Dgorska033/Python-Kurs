W ramach Lesson 20 rozbudowałam projekt Django o routing, dynamiczne
adresy URL, modele, szablony, relacje między modelami, formularze,
filtrowanie danych oraz paginację.

Zadanie 1 -- Statyczne trasy

Dodałam do aplikacji dwa proste adresy URL:

/info/

/rules/

Dla każdej trasy utworzyłam osobny widok funkcyjny. Widoki zwracają
prostą odpowiedź za pomocą HttpResponse.

Przećwiczone elementy: - tworzenie widoków funkcyjnych, -
konfiguracja urls.py, - mapowanie adresu URL na odpowiednią funkcję
widoku.

Zadanie 2 -- Dynamiczna trasa użytkownika

Utworzyłam dynamiczną trasę:

/user/<str:username>/

Django pobiera nazwę użytkownika bezpośrednio z adresu URL i przekazuje
ją jako argument username do funkcji widoku.

Przećwiczone elementy: - dynamiczne parametry URL, - konwerter
<str:username>, - przekazywanie wartości z URL do widoku.

Zadanie 3 -- Model Product

W aplikacji ogloszenia utworzyłam model Product.

Model zawiera pola:

name -- nazwa produktu (CharField),

description -- opis produktu (TextField),

price -- cena produktu (DecimalField).

Dodałam również metodę __str__(), dzięki której obiekt produktu jest
przedstawiany za pomocą jego nazwy.

Po utworzeniu modelu wykonałam migracje bazy danych.

Przećwiczone elementy: - tworzenie modeli Django, - typy pól
modelu, - metoda __str__(), - makemigrations, - migrate.

Zadanie 4 -- Produkty w bazie i lista produktów

Dodałam przykładowe produkty do bazy danych za pomocą Django Shell,
m.in.:

Laptop,

Myszka,

Klawiatura.

Następnie utworzyłam widok pobierający produkty za pomocą:

Product.objects.all()

Dane zostały przekazane do szablonu i wyświetlone na stronie
/products/.

Przećwiczone elementy: - Django Shell, - tworzenie rekordów w
bazie, - Django ORM, - pobieranie wszystkich obiektów modelu, -
przekazywanie danych z widoku do szablonu.

Zadanie 5 -- Dziedziczenie szablonów

Utworzyłam szablon bazowy base.html.

Zdefiniowałam w nim bloki:

{% block title %},

{% block content %}.

Pozostałe szablony mogą dziedziczyć wspólną strukturę za pomocą:

{% extends "ogloszenia/base.html" %}

Przećwiczone elementy: - Django Templates, - dziedziczenie
szablonów, - extends, - block, - organizacja katalogu templates.

Zadanie 6 -- Aplikacja Notatnik

Utworzyłam osobną aplikację Django o nazwie notatnik.

Dodałam model Note zawierający:

title -- tytuł notatki,

content -- treść notatki.

Utworzyłam dwa widoki:

note_list -- lista wszystkich notatek,

note_detail -- szczegóły pojedynczej notatki.

Dodałam trasy:

/notes/

/note/<int:note_id>/

W widoku szczegółów wykorzystałam get_object_or_404(), dzięki czemu
Django zwraca błąd 404, jeżeli notatka o podanym ID nie istnieje.

Przećwiczone elementy: - tworzenie osobnej aplikacji Django, - model
Note, - dynamiczne ID w URL, - get_object_or_404, - widok listy i
szczegółów obiektu.

Zadanie 7 -- Formularz dodawania produktów

Utworzyłam plik forms.py i formularz ProductForm oparty na
forms.ModelForm.

Formularz korzysta z modelu Product i obsługuje pola:

name,

description,

price.

Utworzyłam widok product_create, który:

wyświetla pusty formularz dla żądania GET,

odbiera dane dla żądania POST,

sprawdza poprawność formularza przez form.is_valid(),

zapisuje produkt przez form.save(),

przekierowuje użytkownika do listy produktów.

Dodałam również {% csrf_token %} zabezpieczający formularz POST.

Formularz jest dostępny pod adresem:

/products/add/

Przećwiczone elementy: - ModelForm, - GET i POST, - walidacja
formularza, - zapis do bazy, - redirect, - CSRF, - szablon formularza.

Zadanie 8 -- Relacja Product -- Category

Utworzyłam nowy model Category z polem:

name = models.CharField(max_length=100)

Następnie dodałam do modelu Product relację:

ForeignKey

Produkt może dzięki temu należeć do konkretnej kategorii.

Pole kategorii zostało utworzone jako nullable (null=True), ponieważ w
bazie znajdowały się już wcześniej utworzone produkty, które nie miały
przypisanej kategorii.

Po zmianie modeli wykonałam:

python manage.py makemigrations

oraz:

python manage.py migrate

Przećwiczone elementy: - relacje między tabelami, - ForeignKey, -
klucz obcy, - on_delete, - null=True, - migracja istniejącej bazy po
zmianie modelu.

Zadanie 9 -- Filtrowanie produktów po kategorii

Utworzyłam dynamiczną trasę:

/category/<int:category_id>/

Wartość category_id jest pobierana z adresu URL i przekazywana do
widoku.

Produkty są filtrowane za pomocą Django ORM:

Product.objects.filter(category_id=category_id)

Dzięki temu na stronie wyświetlane są tylko produkty należące do
wskazanej kategorii.

Utworzyłam również szablon products_by_category.html.

Do testowania utworzyłam kategorię Elektronika i przypisałam do niej
istniejące produkty.

Przećwiczone elementy: - filtrowanie QuerySet, - filter(), -
filtrowanie po kluczu obcym, - dynamiczne ID kategorii w URL, -
przekazywanie przefiltrowanych danych do szablonu.

Zadanie 10 -- Paginacja listy notatek

Rozbudowałam widok note_list w aplikacji notatnik o paginację.

Wykorzystałam klasę:

django.core.paginator.Paginator

Ustawiłam maksymalnie 3 notatki na jednej stronie:

Paginator(notes, 3)

Numer aktualnej strony jest pobierany z parametru GET:

request.GET.get('page')

Do szablonu przekazywany jest obiekt page_obj.

W szablonie dodałam obsługę:

page_obj.has_previous,

page_obj.previous_page_number,

page_obj.has_next,

page_obj.next_page_number.

Dzięki temu użytkownik może przechodzić pomiędzy stronami za pomocą
linków Poprzednia i Następna.

Przykład adresu drugiej strony:

/notes/?page=2

Przećwiczone elementy: - Paginator, - parametry GET, - podział
QuerySet na strony, - nawigacja poprzednia/następna, - właściwości
obiektu Page.


Podsumowanie techniczne

W ramach wszystkich zadań wykorzystałam najważniejsze podstawowe
mechanizmy Django:

routing i urls.py,

statyczne i dynamiczne adresy URL,

function-based views,

modele i migracje,

Django ORM,

QuerySet,

all() i filter(),

relacje ForeignKey,

Django Templates,

dziedziczenie szablonów,

formularze ModelForm,

obsługę GET i POST,

CSRF,

przekierowania,

get_object_or_404,

paginację.

Projekt zawiera dwie aplikacje: ogloszenia oraz notatnik. Aplikacja
ogloszenia obsługuje produkty, kategorie, formularz dodawania
produktów i filtrowanie produktów według kategorii. Aplikacja notatnik
obsługuje listę notatek, szczegóły pojedynczej notatki oraz paginację.