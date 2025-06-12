from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import ProfileForm
from .models import CustomUser


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = ProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('profile-edit')

    def get_object(self):
        return self.request.user
