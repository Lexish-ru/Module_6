from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email (логин)")
    avatar = models.ImageField(upload_to="media/", blank=True, null=True, verbose_name="Аватар")
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="Телефон")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Страна")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []