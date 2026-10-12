"""URL-маршруты проекта книжного магазина."""

from django.contrib import admin
from django.urls import path

from shop_app.views import (
    BookCreateView,
    BookDeleteView,
    BookDetailView,
    BookListView,
    BookUpdateView,
)


urlpatterns = [
    path(
        "admin/",
        admin.site.urls,
    ),
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

handler404 = "shop_app.views.custom_page_not_found_view"
handler500 = "shop_app.views.custom_server_error_view"