from django.db import models
from ogloszenia.models import Category

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

    # Czy artykuł jest opublikowany
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    