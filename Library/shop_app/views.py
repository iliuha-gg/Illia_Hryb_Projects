from django.db.models import Count, Q
from django.http import HttpResponse

from .models import Book


def all_books(request):
    """Возвращает список всех книг."""
    books = Book.objects.all()
    return HttpResponse(books)


def filter_books(request):
    """Возвращает книги с ценой от 100 и наличие от 5."""
    books = Book.objects.filter(
        Q(price__gte=100) & Q(stock__gte=5)
    )
    return HttpResponse(books)


def books_with_categories(request):
    """
    Возвращает отфильтрованные книги вместе с их категориями.

    Для каждой книги добавляется количество книг в соответствующей
    категории. Результат сортируется по цене в порядке убывания.
    """
    books = (
        Book.objects.select_related("category")
        .annotate(
            category_books_count=Count("category__books"),
        )
        .filter(
            Q(price__gte=100) & Q(stock__gte=5)
        )
        .order_by("-price")
    )

    return HttpResponse(books)