from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("catalog/", views.catalog_view, name="catalog"),
    path("category/", views.category_list, name="category_list"),
    path("category/<int:pk>/", views.category_view, name="category"),
    path("product/<int:pk>/", views.product_detail, name="product"),
    path("contacts/", views.contacts_view, name="contacts"),
    path("messages/", views.messages_view, name="messages"),
]
