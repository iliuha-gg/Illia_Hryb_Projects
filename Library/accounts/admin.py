"""Настройка административной панели для управления пользователями."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Управляет пользователями, группами и разрешениями в Django Admin."""

    pass