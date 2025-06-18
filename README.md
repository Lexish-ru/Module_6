
# Mailing Service Project

Курсовой проект: сервис email-рассылок  
Django 5 + Bootstrap + PostgreSQL + .env (django-environ)

---

## 🚀 Описание

Сервис позволяет:
- Управлять получателями рассылок (добавлять, редактировать, удалять)
- Управлять шаблонами сообщений
- Создавать и запускать email-рассылки вручную по нужным адресатам
- Сохранять и просматривать попытки отправки писем (лог)
- Вести статистику рассылок на главной
- Регистрировать пользователей, логин/выход, восстановление пароля
- Использовать PostgreSQL и почтовые настройки через .env

---

## 🛠️ Быстрый старт

### 1. Клонировать проект

```bash
git clone https://github.com/Lexish-ru/Module_6.git
cd Module_6
```

### 2. Установить Poetry и зависимости

```bash
poetry install
```

### 3. Подключить виртуальное окружение

```bash
poetry shell
```

### 4. Настроить .env

Создай файл `.env` в корне и добавь свои переменные:

```
SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```
> Для разработки можно включить консольный backend:
> ```
> EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
> ```

### 5. Создать и прогнать миграции

```bash
python manage.py migrate
```

### 6. Создать суперпользователя

```bash
python manage.py createsuperuser
```

### 7. Запустить проект

```bash
python manage.py runserver
```

Открыть [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
Для админки: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📑 Основной функционал

- **Клиенты**: /clients/
- **Сообщения**: /messages/
- **Рассылки**: /mailings/
- **Лог попыток**: /attempts/
- **Регистрация/логин/выход**: /accounts/register/, /accounts/login/, /accounts/logout/
- **Главная (статистика)**: /

---

## ⚙️ Стек технологий

- Python 3.12
- Django 5.x
- Bootstrap 5
- PostgreSQL
- django-environ (.env для конфигов)
- Poetry (управление зависимостями)

---

## 📋 Примечания

- Для реальной отправки писем потребуется рабочий SMTP (gmail/yandex/mail и др.) и разрешённый доступ к SMTP.
- Проект готов для деплоя на любой современный хостинг с поддержкой Python и Postgres.
- Для расширения безопасности используйте HTTPS и храните SECRET_KEY вне гита.

---

## ✍️ Автор

Алексей Столбов  
email: alstoff@live.ru

---
