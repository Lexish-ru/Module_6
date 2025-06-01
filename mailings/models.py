from email.policy import default

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


class Mailing(models.Model):
    STATUS_COICES = [
        ('created', 'Создана'),
        ('started', 'Запущена'),
        ('finished', 'Завершена'),
    ]
    start_at = models.DateTimeField(verbose_name="Дата и время начала")
    end_at = models.DateTimeField(verbose_name="Дата и время окончания")
    status = models.CharField(max_lenght=10, choices=STATUS_COICES, default='created', verbose_name="Статус")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение")
    clients = models.ManyToManyField(Client, related_name="mailings", verbose_name="Получатели")

    def __str__(self):
        return f"Рассылка {self.id} ({self.get_status_display()})"

