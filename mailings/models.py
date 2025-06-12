from email.policy import default
from pyclbr import Class

from django.conf import settings
from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    full_name = models.CharField(max_length=150, verbose_name="ФИО")
    comment = models.TextField(blank=True, verbose_name="Комментарий")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        verbose_name="Владелец"
    )


    class Meta:
        permissions = [
            ("view_all", "Может просматривать все объекты"),
            ("edit_all", "Может редактировать все объекты"),
        ]

    def __str__(self):
        return f"{self.full_name} <{self.email}>"


class Message(models.Model):
    subject = models.CharField(max_length=200, verbose_name="Тeма")
    body = models.TextField(verbose_name="Текст сообщения")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        verbose_name="Владелец",)


    class Meta:
        permissions = [
            ("view_all", "Может просматривать все объекты"),
            ("edit_all", "Может редактировать все объекты"),
        ]

    def __str__(self):
        return self.subject


class Mailing(models.Model):
    STATUS_COICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('finished', 'Завершена'),
    ]
    start_at = models.DateTimeField(verbose_name="Дата и время начала")
    end_at = models.DateTimeField(verbose_name="Дата и время окончания")
    status = models.CharField(max_length=10, choices=STATUS_COICES, default='created', verbose_name="Статус")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    clients = models.ManyToManyField(Client, related_name="mailings", verbose_name="Получатели")
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        verbose_name="Владелец",)


    class Meta:
        permissions = [
            ("view_all", "Может просматривать все объекты"),
            ("edit_all", "Может редактировать все объекты"),
        ]

    def __str__(self):
        return f"Рассылка {self.id} ({self.get_status_display()})"


class MailingAttempt(models.Model):
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name="attempts", verbose_name="Рассылка")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Получатель")
    attempted_at = models.DateTimeField(auto_now_add=True, verbose_name="Время попытки")
    status = models.CharField (max_length=20, verbose_name="Статус попытки")
    server_response = models.TextField(verbose_name="Ответ сервера", blank=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        verbose_name="Владелец",)

    class Meta:
        permissions = [
            ("view_all", "Может просматривать все объекты"),
            ("edit_all", "Может редактировать все объекты"),
        ]

    def __str__(self):
        return f"{self.mailing} -> {self.client} [{self.status}]"
