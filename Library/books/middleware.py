"""Промежуточный обработчик HTTP-запросов приложения."""

import logging
import time


logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    """Логирует HTTP-запросы и время их обработки."""

    def __init__(self, get_response):
        """Сохраняет обработчик следующего компонента Django."""
        self.get_response = get_response

    def __call__(self, request):
        """Обрабатывает запрос и записывает результат в лог."""
        start_time = time.perf_counter()

        response = self.get_response(request)

        duration = (
            time.perf_counter() - start_time
        ) * 1000

        logger.info(
            "%s %s | Status: %s | Duration: %.2f ms",
            request.method,
            request.path,
            response.status_code,
            duration,
        )

        return response