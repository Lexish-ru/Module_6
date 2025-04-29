# catalog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from .forms import MessageForm


def home_view(request):
    products = Product.objects.all()
    return render(request, "catalog/index.html", {"products": products})



def catalog_view(request):
    products = Product.objects.all()
    return render(request, "catalog/catalog.html", {"products": products})


def category_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, "catalog/category.html", {
        "category": category,
        "products": products
    })


def category_list(request):
    categories = Category.objects.all()
    return render(request, "catalog/category.html", {"categories": categories})


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "catalog/product.html", {"product": product})


def contacts_view(request):
    form = MessageForm()
    return render(request, "catalog/contacts.html", {"form": form})

def contacts_view(request):
    success = False
    name = ""
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            success = True
            name = message.name
            form = MessageForm()  # сбрасываем форму
    else:
        form = MessageForm()

    return render(request, "catalog/contacts.html", {
        "form": form,
        "success": success,
        "name": name
    })

def messages_view(request):
    return render(request, "catalog/messages.html")
