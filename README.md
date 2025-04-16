# Django Retro Market

Проект "Ретро-Маркет" на Django — учебное приложение, имитирующее витрину техники прошлых лет: ретро-смартфоны, игровые консоли, MP3-плееры. Содержит несколько страниц с шаблонами, навигацией и формой обратной связи.

## 🔧 Стек

- Python 3.12
- Django (через Poetry)
- HTML / Bootstrap
- Jinja2-шаблоны

## 📦 Установка

1. Клонировать репозиторий:

```bash
git clone https://github.com/yourusername/django-retro.git
cd django-retro
```

2. Установить зависимости через Poetry:

```bash
poetry install
```

3. Запустить сервер:

```bash
poetry run python manage.py runserver
```

## 🗂 Страницы

- `/` — главная
- `/catalog/` — каталог категорий
- `/category/` — ретро-смартфоны
- `/contacts/` — форма обратной связи

## 📁 Структура

```
catalog/
├── views.py
├── urls.py
├── templates/
│   └── catalog/
│       ├── index.html
│       ├── catalog.html
│       ├── category.html
│       └── contacts.html
config/
├── settings.py
├── urls.py
manage.py
pyproject.toml
poetry.lock
```

## 🧪 Заметки

- Форма на странице `/contacts/` пока не сохраняет данные, но обрабатывает отправку.
- Bootstrap подключён через CDN.

## 📜 Лицензия

Проект создан в учебных целях. Использование по назначению — приветствуется.