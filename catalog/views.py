from django.shortcuts import render
from .models import Message


def home(request):
    return render(request, 'catalog/index.html')

def catalog_view(request):
    return render(request, 'catalog/catalog.html')

def category_view(request):
    return render(request, 'catalog/category.html')

def contacts_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "Без имени")
        email = request.POST.get("email", "Без почты")
        message = request.POST.get("message", "Без сообщения")

        print("Новое сообщение:")
        print(f"Имя: {name}")
        print(f"Email: {email}")
        print(f"Сообщение: {message}")

        return render(request, 'catalog/contacts.html', {
            "success": True,
            "name": name
        })

    return render(request, 'catalog/contacts.html')

