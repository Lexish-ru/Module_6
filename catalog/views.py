from django.views.generic import TemplateView, ListView, DetailView, FormView
from django.shortcuts import get_object_or_404
from .models import Product, Category
from .forms import MessageForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Product
    template_name = "catalog/index.html"
    context_object_name = "products"

class CatalogView(ListView):
    model = Product
    template_name = "catalog/catalog.html"
    context_object_name = "products"

class CategoryDetailView(DetailView):
    model = Category
    template_name = "catalog/category.html"
    context_object_name = "category"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=self.object)
        return context

class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category.html"
    context_object_name = "categories"

class ProductDetailView(DetailView):
    model = Product
    template_name = "catalog/product.html"
    context_object_name = "product"

class ContactsView(FormView):
    template_name = "catalog/contacts.html"
    form_class = MessageForm
    success_url = reverse_lazy("contacts")

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(success=True, name=self.object.name, form=self.form_class()))