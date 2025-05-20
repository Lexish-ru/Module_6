from django.urls import path
from .views import (
    HomeView,
    CatalogView,
    CategoryDetailView,
    CategoryListView,
    ProductDetailView,
    ContactsView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("catalog/", CatalogView.as_view(), name="catalog"),
    path("category/", CategoryListView.as_view(), name="category_list"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
]