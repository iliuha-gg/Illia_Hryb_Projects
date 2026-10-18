"""URL-маршруты приложения книжного магазина."""

from django.urls import path

from .views import (
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
)


urlpatterns = [
    path(
        "",
        BookListView.as_view(),
        name="home",
    ),
    path(
        "books/",
        BookListView.as_view(),
        name="book_list",
    ),
    path(
        "books/create/",
        BookCreateView.as_view(),
        name="book_create",
    ),
    path(
        "books/<int:pk>/",
        BookDetailView.as_view(),
        name="book_detail",
    ),
    path(
        "books/<int:pk>/update/",
        BookUpdateView.as_view(),
        name="book_update",
    ),
    path(
        "books/<int:pk>/delete/",
        BookDeleteView.as_view(),
        name="book_delete",
    ),
]