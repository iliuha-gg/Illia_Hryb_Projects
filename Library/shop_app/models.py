from django.conf import settings
from django.db import models


class Category(models.Model):
    """Модель категории книг."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self) -> str:
        """Возвращает название категории."""
        return self.name


class Book(models.Model):
    """Модель книги в магазине."""

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books",
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    description = models.TextField()
    stock = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="books",
    )

    def __str__(self) -> str:
        """Возвращает название книги."""
        return self.title