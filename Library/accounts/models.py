from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=11, unique=True, blank=True),
    date_of_birth = models.DateField(null=True, blank=True)