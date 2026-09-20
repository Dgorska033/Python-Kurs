from django.contrib import admin
from .models import Ogloszenie


# Konfiguracja sposobu wyświetlania ogłoszeń w panelu admina
class OgloszenieAdmin(admin.ModelAdmin):
    # Kolumny widoczne na liście ogłoszeń
    list_display = ('tytul', 'cena', 'data_dodania')


# Rejestracja modelu Ogloszenie wraz z jego konfiguracją
admin.site.register(Ogloszenie, OgloszenieAdmin)