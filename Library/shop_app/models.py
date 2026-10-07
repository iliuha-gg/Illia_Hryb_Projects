from django.db import models


class Category(models.Model):
    """Модель категории книг."""

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        """Возвращает название категории."""
        return self.name


class Book(models.Model):
    """Модель книги интернет-магазина."""

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()

    # Каждая книга относится к одной категории.
    # При удалении категории связанные книги также будут удалены.
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='books'
    )

    def __str__(self):
        """Возвращает название книги."""
        return self.title