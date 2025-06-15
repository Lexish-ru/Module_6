import logging

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ClientForm, MailingForm, MessageForm
from .models import Client, Mailing, MailingAttempt, Message

# Create your views here.

logger = logging.getLogger(__name__)

@cache_page(60 * 5)
def home(request):
    """Главная страница сервиса рассылок."""
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(status='started').count()
    unique_clients = Client.objects.count()
    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients
    }
    return render(request, 'mailings/home.html', context)


@method_decorator(cache_page(60*5), name='dispatch')
class ClientListView(ListView):
    """
    Представление для списка клиентов.
    Если пользователь менеджер (is_staff), видит всех, иначе — только своих.
    """
    model = Client
    template_name = 'mailings/client_list.html'

    def get_queryset(self):
        """
        Возвращает QuerySet клиентов: всех для менеджера, или только своих.
        """
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs  # менеджеры видят всё
        return qs.filter(owner=self.request.user)


class ClientCreateView(CreateView):
    """Создание нового клиента рассылки."""
    model = Client
    form_class = ClientForm
    template_name = 'mailings/client_form.html'
    success_url = reverse_lazy('client-list')

    def form_valid(self, form):
        """
         Устанавливает текущего пользователя владельцем клиента.
        """
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ClientUpdateView(UpdateView):
    """Редактирование клиента рассылки."""
    model = Client
    form_class = ClientForm
    template_name = 'mailings/client_form.html'
    success_url = reverse_lazy('client-list')

    def get_queryset(self):
        """Ограничивает доступ к клиентам."""
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(owner=self.request.user)


class ClientDeleteView(DeleteView):
    """Удаление клиента рассылки."""
    model = Client
    template_name = 'mailings/client_confirm_delete.html'
    success_url = reverse_lazy('client-list')

    def get_queryset(self):
        """Ограничивает доступ к клиентам."""
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(owner=self.request.user)



@method_decorator(cache_page(60*5), name='dispatch')
class MessageListView(ListView):
    """Список сообщений для рассылки."""
    model = Message
    template_name = 'mailings/message_list.html'

    def get_queryset(self):
        """Показывает сообщения только владельца или все для менеджера."""
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(owner=self.request.user)

class MessageCreateView(CreateView):
    """Создание сообщения для рассылки."""
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('message-list')

    def form_valid(self, form):
        """Устанавливает текущего пользователя владельцем сообщения."""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    """Редактирование сообщения для рассылки."""
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('message-list')

    def get_queryset(self):
        """Ограничивает доступ к сообщениям."""
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(owner=self.request.user)


class MessageDeleteView(DeleteView):
    """Удаление сообщения для рассылки."""
    model = Message
    template_name = 'mailings/message_confirm_delete.html'
    success_url = reverse_lazy('message-list')

    def get_queryset(self):
        """Ограничивает доступ к сообщениям."""
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(owner=self.request.user)



@method_decorator(cache_page(60*5), name='dispatch')
class MailingListView(ListView):
    """Список рассылок для пользователя."""
    model = Mailing
    template_name = 'mailing/mailing_list.html'

    def get_queryset(self):
        """Показывает рассылки только владельца или все для менеджера."""
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs  # менеджеры видят всё
        return qs.filter(owner=self.request.user)


class MailingCreateView(CreateView):
    """Создание новой рассылки."""
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailing-list')

    def form_valid(self, form):
        """Устанавливает текущего пользователя владельцем рассылки."""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class MailingUpdateView(UpdateView):
    """Редактирование рассылки."""
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailing-list')

    def get_queryset(self):
        """Ограничивает доступ к своим рассылкам."""
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(owner=self.request.user)


class MailingDeleteView(DeleteView):
    """Удаление рассылки."""
    model = Mailing
    template_name = 'mailings/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailing-list')

    def get_queryset(self):
        """Ограничивает доступ к своим рассылкам."""
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(owner=self.request.user)


@method_decorator(cache_page(60*5), name='dispatch')
class MailingStartView(View):
    """
    Запуск рассылки для выбранной группы клиентов.
    Формирует MailingAttempt для каждого получателя.
    """
    def post(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        logger.info(f"Пользователь {request.user.email} запускает рассылку id={mailing.id}")
        if mailing.status != "created":
            messages.error(request, "Рассылка уже запущена или завершена.")
            logger.warning(f"Рассылка {mailing.id} уже была запущена/завершена")
            return redirect('mailing-list')
        clients = mailing.clients.all()
        results = []
        for client in clients:
            try:
                send_mail(
                    subject=mailing.message.subject,
                    message=mailing.message.body,
                    from_email='EMAIL_HOST_USER',
                    recipient_list=[client.email],
                    fail_silently=False
                )
                status = 'Успешно'
                server_response = 'ok'
                logger.info(f"Письмо отправлено на {client.email}")
            except Exception as e:
                status = "Неудача"
                server_response = str(e)
                logger.error(f"Ошибка отправки {client.email}: {e}")
            MailingAttempt.objects.create(
                mailing=mailing,
                client=client,
                attempted_at=timezone.now(),
                status=status,
                server_response=server_response,
                owner=request.user
            )
            results.append((client.email, status))
        mailing.status = 'started'
        mailing.save()
        messages.success(request, "Рассылка запущена. Отправлено {} писем.".format(len(results)))
        logger.info(f"Рассылка {mailing.id} завершена: {len(results)} писем отправлено")
        return redirect('mailing-list')



@method_decorator(cache_page(60*5), name='dispatch')
class MailingAttemptListView(ListView):
    """Список попыток рассылок (отчёт)."""
    model = MailingAttempt
    template_name = 'mailings/attempt_list.html'
    context_object_name = 'attempts'
    ordering = ['-attempted_at']

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_staff:
            return qs
        return qs.filter(owner=self.request.user)


class RegisterView(CreateView):
    """Создание пользователя"""
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
