from django.contrib import admin

from .models import Book, Category


class BookInline(admin.TabularInline):
    """Позволяет редактировать книги прямо на странице категории."""

    model = Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Настраивает отображение категорий в административной панели."""

    inlines = [BookInline]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Настраивает отображение, фильтрацию и поиск книг в админ-панели."""

    # Поля, отображаемые в списке книг.
    list_display = (
        "title",
        "author",
        "price",
        "stock",
        "category",
    )

    # Поля, доступные для фильтрации.
    list_filter = (
        "category",
    )

    # Поля, по которым выполняется поиск.
    search_fields = (
        "title",
        "author",
    )