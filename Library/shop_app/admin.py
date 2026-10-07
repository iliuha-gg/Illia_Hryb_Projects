from django.contrib import admin

from .models import Book, Category


class BookInline(admin.TabularInline):
    """Позволяет редактировать книги прямо на странице категории."""

    model = Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настройки отображения модели Category в административной панели."""

    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Настройки отображения и поиска книг в административной панели."""

    # Поля, которые отображаются в списке книг.
    list_display = (
        'title',
        'author',
        'price',
        'stock',
        'category',
    )

    # Фильтрация списка книг по категории.
    list_filter = (
        'category',
    )

    # Поиск книг по названию и автору.
    search_fields = (
        'title',
        'author',
    )