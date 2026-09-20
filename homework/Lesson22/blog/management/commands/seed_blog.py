from django.core.management.base import BaseCommand
from faker import Faker
import random

from blog.models import Category, Post, Tag


class Command(BaseCommand):
    help = 'Tworzy kategorie, tagi oraz 100 losowych postów'

    def handle(self, *args, **options):

        # Faker generujący polskie dane
        fake = Faker('pl_PL')


        # -----------------------------------
        # 1. Usuwamy stare dane
        # -----------------------------------

        Post.objects.all().delete()
        Category.objects.all().delete()
        Tag.objects.all().delete()

        self.stdout.write(
            'Usunięto stare posty, kategorie i tagi.'
        )


        # -----------------------------------
        # 2. Tworzymy kategorie
        # -----------------------------------

        category_names = [
            'Technologia',
            'Podróże',
            'Kulinaria',
            'Sport',
            'Muzyka',
            'Filmy',
            'Nauka'
        ]

        categories = []

        for name in category_names:
            category = Category.objects.create(name=name)
            categories.append(category)

        self.stdout.write('Utworzono kategorie.')


        # -----------------------------------
        # 3. Tworzymy tagi
        # -----------------------------------

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

        tags = []

        for name in tag_names:
            tag = Tag.objects.create(name=name)
            tags.append(tag)

        self.stdout.write('Utworzono tagi.')


        # -----------------------------------
        # 4. Tworzymy 100 postów
        # -----------------------------------

        for i in range(100):

            post = Post.objects.create(
                title=fake.sentence(nb_words=6),
                content=fake.text(),
                category=random.choice(categories)
            )


            # -----------------------------------
            # 5. Losujemy od 1 do 5 tagów
            # -----------------------------------

            random_tags = random.sample(
                tags,
                k=random.randint(1, 5)
            )

            # Przypisujemy wylosowane tagi do posta
            post.tags.set(random_tags)


        self.stdout.write(
            self.style.SUCCESS(
                'Gotowe! Utworzono 100 postów z losowymi tagami.'
            )
        )