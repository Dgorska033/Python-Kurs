from django.shortcuts import render
from .models import Category, Post
from django.db.models import Q

# Widok wyświetlający posty należące do wybranej kategorii
def category_posts(request, category_id):


    # Pobieramy kategorię o konkretnym ID
    category = Category.objects.get(id=category_id)

    # Pobieramy tylko posty należące do tej kategorii
    posts = Post.objects.filter(category=category)

    # Przekazujemy kategorię i posty do szablonu HTML
    return render(
        request,
        'blog/category_posts.html',
        {
            'category': category,
            'posts': posts
        }
    )

# Widok strony głównej
def home(request):

    # Pobieramy posty od najnowszego
    # i ograniczamy wynik tylko do pierwszych 5
    posts = Post.objects.order_by('-publication_date')[:5] # Post objects pracuje na modelu POST 
                                                        #.order_by('-publication_date') sortuje po publication_date
                                                        # (-) przed publication daje oznacza sortowanie malejąco
                                                        # [:5] slicing - daj mi 5 najnowszych postów.
    return render(
        request,
        'blog/home.html',
        {'posts': posts}
    )

# Widok wyszukiwarki postów
def search_posts(request):

    # Pobieramy frazę "q" z adresu URL
    query = request.GET.get('q', '')

    # Szukamy frazy w tytule LUB w treści posta
    posts = Post.objects.filter(
        Q(title__icontains=query) |
        Q(content__icontains=query)
    )

    # Przekazujemy wyniki i szukaną frazę do HTML
    return render(
        request,
        'blog/search_results.html',
        {
            'posts': posts,
            'query': query
        }
    )