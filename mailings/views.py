from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ClientForm, MessageForm, MailingForm
from .models import Client, Message, Mailing

# Create your views here.

def home(request):
    return render(request, 'mailings/home.html')

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

