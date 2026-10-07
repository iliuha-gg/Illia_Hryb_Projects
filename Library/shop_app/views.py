from django.http import HttpResponse
from django.db.models import Count, Q

from .models import Book


def all_books(request):
    books = Book.objects.all()

    return HttpResponse(books)


def filter_books(request):
    books = Book.objects.filter(
        Q(price__gte=100) & Q(stock__gte=5)
    )

    return HttpResponse(books)


def books_with_categories(request):
    books = (
        Book.objects
        .select_related('category')
        .annotate(
            category_books_count=Count('category__books')
        )
        .filter(
            Q(price__gte=100) & Q(stock__gte=5)
        )
        .order_by('-price')
    )

    return HttpResponse(books)