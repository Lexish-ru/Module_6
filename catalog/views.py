from django.views.generic import DetailView, FormView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404
from .models import Product, Category
from .forms import MessageForm, ProductForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["can_edit"] = (
                user.is_authenticated and (user == self.object.owner or user.has_perm("catalog.can_unpublish_product"))
        )
        return context


class ContactsView(FormView):
    template_name = "catalog/contacts.html"
    form_class = MessageForm
    success_url = reverse_lazy("contacts")

    def form_valid(self, form):
        self.object = form.save()
        return self.render_to_response(self.get_context_data(success=True, name=self.object.name, form=self.form_class()))


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/catalog.html'
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog')
