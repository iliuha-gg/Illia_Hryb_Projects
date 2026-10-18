"""Главные URL-маршруты проекта."""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from debug_toolbar.toolbar import debug_toolbar_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls")),
    path("", include("accounts.urls")),

]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()

handler404 = "books.views.custom_page_not_found_view"
handler500 = "books.views.custom_server_error_view"