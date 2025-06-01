from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    comment = models.TextField(blank=True, verbose_name="Комментарий")

    def __str__(self):
        return f"{self.full_name} <{self.email}>"


class Message(models.Model):
    subject = models.CharField(max_leghth=200, verbose_name="Тeма")
    body = models.TextField(verbose_name="Текст сообщения")

    def __str__(self):
        return self.subject


