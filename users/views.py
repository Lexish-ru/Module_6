from django.contrib.auth import login
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from .models import User

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)  # Автоматический вход
        return response

