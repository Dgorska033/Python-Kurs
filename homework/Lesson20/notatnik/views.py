from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Note

# # Lista wszystkich notatek
# def note_list(request):
#     notes = Note.objects.all()

#     return render(
#         request,
#         'notatnik/note_list.html',
#         {'notes': notes}
#     )


# # Szczegóły pojedynczej notatki
# def note_detail(request, note_id):
#     note = get_object_or_404(Note, id=note_id)

#     return render(
#         request,
#         'notatnik/note_detail.html',
#         {'note': note}
#     )


# Lista wszystkich notatek z paginacją
def note_list(request):
    # Pobieramy wszystkie notatki
    notes = Note.objects.all()

    # Maksymalnie 3 notatki na jednej stronie
    paginator = Paginator(notes, 3)

    # Pobieramy numer strony z adresu, np. ?page=2
    page_number = request.GET.get('page')

    # Pobieramy notatki należące do wybranej strony
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'notatnik/note_list.html',
        {'page_obj': page_obj}
    )


# Szczegóły pojedynczej notatki
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    return render(
        request,
        'notatnik/note_detail.html',
        {'note': note}
    )



