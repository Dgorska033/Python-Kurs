from django.db import models


# Model pojedynczej notatki
class Note(models.Model):

    # Tytuł notatki
    title = models.CharField(max_length=100)

    # Treść notatki
    content = models.TextField()

    def __str__(self):
        return self.title