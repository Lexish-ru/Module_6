from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Очистить базу и загрузить тестовые данные из фикстур'

    def handle(self, *args, **kwargs):
        self.stdout.write('Удаление старых данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write('Импорт новых данных из фикстур...')
        call_command('loaddata', 'categories.json')
        call_command('loaddata', 'products.json')

        self.stdout.write(self.style.SUCCESS('Тестовые данные успешно загружены!'))
