from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # Adresy URL aplikacji blog
    path('', include('blog.urls')), #include('blog.urls') = oprócz URL-i znajdujących się tutaj sprawdzaj również blog/urls.p


    # Rejestracja, logowanie, wylogowanie itd.
    path('accounts/', include('allauth.urls')),
]

include('blog.urls') 