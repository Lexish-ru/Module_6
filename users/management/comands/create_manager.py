from django.core.management.base import BaseCommand
from users.models import CustomUser
from django.contrib.auth.models import Group

class Command(BaseCommand):
    """Создаёт пользователя-менеджера с группой 'Менеджер'."""

    help = 'Создать пользователя с правами менеджера'

    def handle(self, *args, **options):
        email = 'manager@example.com'
        password = '12345678'
        if CustomUser.objects.filter(email=email).exists():
            self.stdout.write(self.style.WARNING('Пользователь уже существует!'))
            return
        user = CustomUser.objects.create_user(email=email, password=password, is_staff=True)
        group, created = Group.objects.get_or_create(name='Менеджер')
        user.groups.add(group)
        self.stdout.write(self.style.SUCCESS(f'Менеджер создан: {email} / {password}'))
