import logging

from django.http import HttpResponseForbidden


logger = logging.getLogger(__name__)


class AuthorRequiredMixin:
    """Разрешает изменение объекта только его автору."""

    def dispatch(self, request, *args, **kwargs):
        """Проверяет, является ли текущий пользователь автором объекта."""
        book = self.get_object()

        if book.author != request.user:
            return HttpResponseForbidden(
                "You are not the author of this book."
            )

        return super().dispatch(request, *args, **kwargs)


class InStockOnlyMixin:
    """Показывает только книги, которые есть в наличии."""

    def get_queryset(self):
        """Возвращает книги с количеством на складе больше нуля."""
        return super().get_queryset().filter(stock__gt=0)


class ActionLogMixin:
    """Логирует пользователя, представление и HTTP-метод запроса."""

    def dispatch(self, request, *args, **kwargs):
        """Записывает информацию о запросе в лог."""
        logger.info(
            "%s opened %s with %s request",
            request.user,
            self.__class__.__name__,
            request.method,
        )

        return super().dispatch(request, *args, **kwargs)


class AuthorMixin:
    """Автоматически назначает текущего пользователя автором объекта."""

    def form_valid(self, form):
        """Назначает текущего пользователя автором перед сохранением."""
        form.instance.author = self.request.user
        return super().form_valid(form)