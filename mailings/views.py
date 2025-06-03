from django.shortcuts import render,get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib import messages
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.views import View

from .forms import ClientForm, MailingForm, MessageForm
from .models import Client, Mailing, Message, MailingAttempt

# Create your views here.

def home(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(status='started').count()
    unique_clients = Client.objects.count()
    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'unique_clients': unique_clients
    }
    return render(request, 'mailings/home.html', context)

class ClientListView(ListView):
    model = Client
    template_name = 'mailings/client_list.html'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailings/client_form.html'
    success_url = reverse_lazy('client-list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'mailings/client_form.html'
    success_url = reverse_lazy('client-list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'mailings/client_confirm_delete.html'
    success_url = reverse_lazy('client-list')

class MessageListView(ListView):
    model = Message
    template_name = 'mailings/message_list.html'

class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('message-list')

class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'mailings/message_form.html'
    success_url = reverse_lazy('message-list')

class MessageDeleteView(DeleteView):
    model = Message
    template_name = 'mailings/message_confirm_delete.html'
    success_url = reverse_lazy('message-list')

class MailingListView(ListView):
    model = Mailing
    template_name = 'mailing/mailing_list.html'

class MailingCreateView(CreateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailing-list')

class MailingUpdateView(UpdateView):
    model = Mailing
    form_class = MailingForm
    template_name = 'mailings/mailing_form.html'
    success_url = reverse_lazy('mailing-list')

class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = 'mailings/mailing_confirm_delete.html'
    success_url = reverse_lazy('mailing-list')

class MailingStartView(View):
    def post(self, request, pk):
        mailing = get_object_or_404(Mailing, pk=pk)
        if mailing.status != "created":
            messages.error(request, "Рассылка уже запущена или завершена.")
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
            except Exception as e:
                status = "Неудача"
                server_response = str(e)

            MailingAttempt.objects.create(
                mailing=mailing,
                client=client,
                attempted_at=timezone.now(),
                status=status,
                server_response=server_response,
            )
            results.append((client.email, status))

        mailing.status = 'started'
        mailing.save()
        messages.success(request, "Рассылка запущена. Отправлено {} писем.".format(len(results)))
        return redirect('mailing-list')

class MailingAttemptListView(ListView):
    model = MailingAttempt
    template_name = 'mailings/attempt_list.html'
    context_object_name = 'attempts'
    ordering = ['-attempted_at']

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
