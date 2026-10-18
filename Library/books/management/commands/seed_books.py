import random

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from books.models import Book, Category


User = get_user_model()


class Command(BaseCommand):
    """Заполняет базу тестовыми категориями и книгами."""

    help = "Создаёт тестовые категории и книги."

    def handle(self, *args, **options):
        """Создаёт тестовые данные для книжного магазина."""
        user, _ = User.objects.get_or_create(
            username="demo_user",
        )

        categories_data = [
            ("Fantasy", "fantasy"),
            ("Science", "science"),
            ("History", "history"),
            ("Programming", "programming"),
            ("Business", "business"),
        ]

        categories = []

        for name, slug in categories_data:
            category, _ = Category.objects.get_or_create(
                slug=slug,
                defaults={
                    "name": name,
                },
            )
            categories.append(category)

        titles = [
            "Python Fundamentals",
            "Django in Practice",
            "Artificial Intelligence Basics",
            "The Lost Kingdom",
            "History of Europe",
            "Modern Business",
            "Machine Learning Guide",
            "Fantasy World",
            "Web Development",
            "Data Science Essentials",
            "Deep Learning",
            "Clean Python",
            "Algorithms and Data Structures",
            "Future Technologies",
            "Software Engineering",
        ]

        for title in titles:
            Book.objects.get_or_create(
                title=title,
                defaults={
                    "author": user,
                    "price": random.randint(10, 150),
                    "description": (
                        f"Описание книги {title}."
                    ),
                    "stock": random.randint(0, 20),
                    "category": random.choice(categories),
                },
            )

        self.stdout.write(
            self.style.SUCCESS(
                "База данных успешно заполнена."
            )
        )