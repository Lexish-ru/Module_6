from django import forms

from .models import CustomUser


class ProfileForm(forms.ModelForm):
    """Форма для редактирования профиля пользователя."""
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'avatar', 'phone', 'country']

    def __init__(self, *args, **kwargs):
        """
        Добавляет класс Bootstrap к полям формы.
        """
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
