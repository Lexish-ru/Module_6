from django.shortcuts import render
from .models import Message, Product
from .forms import MessageForm


def home(request):
    products = Product.objects.all()
    return render(request, 'catalog/index.html', {'products': products})

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

def messages_view(request):
    messages = Message.objects.order_by('-created_at')
    return render(request, 'catalog/messages.html', {'messages': messages})


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'catalog/product.html', {'product': product})
