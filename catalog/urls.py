# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('category/', views.category_view, name='category'),
    path('contacts/', views.contacts_view, name='contacts'),
]
