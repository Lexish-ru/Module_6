from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from .models import User

class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')  # или 'catalog'
