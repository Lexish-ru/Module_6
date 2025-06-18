from email.policy import default
from pyclbr import Class

from django.conf import settings
from django.db import models


class Client(models.Model):
    """
    Получатель рассылки (клиент).
    Содержит email, ФИО, комментарий, владельца.
    """
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
        """Строковое представление клиента."""
        return f"{self.full_name} <{self.email}>"


class Message(models.Model):
    """
    Сообщение для рассылки.
    Содержит тему, тело письма и владельца.
    """
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
        """Строковое представление сообщения."""
        return self.subject


class Mailing(models.Model):
    """
    Модель рассылки.
    Хранит дату/время старта и окончания, статус, сообщение и клиентов, владельца.
    """
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
        """Строковое представление рассылки."""
        return f"Рассылка {self.id} ({self.get_status_display()})"


class MailingAttempt(models.Model):
    """
    Попытка отправки сообщения по рассылке.
    Содержит дату, статус, ответ сервера, ссылку на рассылку и владельца.
    """
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
        """Строковое представление попытки отправки."""
        return f"{self.mailing} -> {self.client} [{self.status}]"
