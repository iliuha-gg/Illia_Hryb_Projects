from django.core.management.base import BaseCommand

from shop_app.models import Category


class Command(BaseCommand):
    """Создаёт тестовые категории книг."""

    help = "Создаёт категории книг."

    def handle(self, *args, **options):
        """Добавляет категории в базу данных."""
        categories = [
            ("Fantasy", "fantasy"),
            ("Science Fiction", "science-fiction"),
            ("History", "history"),
            ("Programming", "programming"),
            ("Business", "business"),
        ]

        created_count = 0

        for name, slug in categories:
            _, created = Category.objects.get_or_create(
                slug=slug,
                defaults={
                    "name": name,
                },
            )

            if created:
                created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Создано категорий: {created_count}"
            )
        )