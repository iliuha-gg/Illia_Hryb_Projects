from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BookForm
from .mixins import (
    ActionLogMixin,
    InStockOnlyMixin,
    AuthorMixin,
)
from .models import Book, Category


def custom_page_not_found_view(request, exception):
    """Отображает пользовательскую страницу ошибки 404."""
    return render(
        request,
        "error/404.html",
        status=404,
    )


def custom_server_error_view(request):
    """Отображает пользовательскую страницу ошибки 500."""
    return render(
        request,
        "error/500.html",
        status=500,
    )


class BookListView(
    ActionLogMixin,
    InStockOnlyMixin,
    ListView,
):
    """Отображает список книг с фильтрацией по категории."""

    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    paginate_by = 10

    def get_queryset(self):
        """Возвращает книги с учётом выбранной категории."""
        queryset = super().get_queryset()

        category = self.request.GET.get("category")

        if category:
            queryset = queryset.filter(
                category__slug=category,
            )

        return queryset

    def get_context_data(self, **kwargs):
        """Добавляет категории в контекст шаблона."""
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class BookDetailView(
    ActionLogMixin,
    DetailView,
):
    """Отображает подробную информацию о книге."""

    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


class BookCreateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ActionLogMixin,
    AuthorMixin,
    CreateView,
):
    """Создаёт новую книгу для авторизованного пользователя."""

    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")
    permission_required = "books.add_book"


class BookUpdateView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ActionLogMixin,
    UpdateView,
):
    """Позволяет автору редактировать свою книгу."""

    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("book_list")
    permission_required = "books.change_book"


class BookDeleteView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    ActionLogMixin,
    DeleteView,
):
    """Позволяет автору удалить свою книгу."""

    model = Book
    template_name = "books/book_confirm_delete.html"
    context_object_name = "book"
    success_url = reverse_lazy("book_list")
    permission_required = "books.delete_book"