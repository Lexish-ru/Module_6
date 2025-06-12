from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email должен быть задан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')
        return self.create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Email (логин)")
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Имя")
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="Фамилия")
    avatar = models.ImageField(upload_to="media/", blank=True, null=True, verbose_name="Аватар")
    phone = models.CharField(max_length=30, blank=True, null=True, verbose_name="Телефон")
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Страна")
    objects = CustomUserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


