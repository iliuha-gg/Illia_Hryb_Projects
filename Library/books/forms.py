from django import forms

from .models import Book


class BookForm(forms.ModelForm):
    """Форма для создания и редактирования книги."""

    class Meta:
        """Настройки формы книги."""

        model = Book
        fields = (
            "title",
            "price",
            "description",
            "stock",
            "category",
        )
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "step": "0.01",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                }
            ),
            "stock": forms.NumberInput(
                attrs={
                    "class": "form-control",
                }
            ),
            "category": forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
        }