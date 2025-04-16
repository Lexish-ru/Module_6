from django.shortcuts import render
from .models import Message
from .forms import MessageForm


def home(request):
    return render(request, 'catalog/index.html')

def catalog_view(request):
    return render(request, 'catalog/catalog.html')

def category_view(request):
    return render(request, 'catalog/category.html')

def contacts_view(request):
    form = MessageForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return render(request, 'catalog/contacts.html', {
            "success": True,
            "name": form.cleaned_data.get("name"),
            "form": MessageForm()  # новая пустая форма после отправки
        })

    return render(request, 'catalog/contacts.html', {
        "form": form
    })
