from datetime import timedelta

from django.shortcuts import render
from django.utils import timezone

from .models import Article


def article_list_view(request):

    # Pobieramy tylko opublikowane artykuły
    articles = Article.objects.filter(
        is_published=True
    ).order_by('-pub_date')

    # Pobieramy z adresu parametr q, czyli szukaną frazę
    query = request.GET.get('q')

    # Jeśli użytkownik coś wpisał, filtrujemy artykuły po tytule
    if query:
        articles = articles.filter(
            title__icontains=query      # icontains = tytuł zawiera ten tekst, bez zwracania uwagi na wielkość liter
        )

    # Data sprzed 3 dni - potrzebna do napisu "NOWOŚĆ!"
    three_days_ago = timezone.now() - timedelta(days=3)

    context = {
        'articles': articles,
        'three_days_ago': three_days_ago,
        'query': query,
    }

    return render(
        request,
        'articles/article_list.html',
        context
    )