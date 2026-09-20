from django.db import models


# Model kategorii postów
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model tagu
class Tag(models.Model):
    # Nazwa tagu, np. Python, Django, AI
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Model posta na blogu
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)

    # Jeden post należy do jednej kategorii
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    # Jeden post może mieć wiele tagów,
    # a jeden tag może należeć do wielu postów
    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__(self):
        return self.title