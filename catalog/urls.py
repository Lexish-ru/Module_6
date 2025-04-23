# catalog/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog_view, name='catalog'),
    path('category/', views.category_view, name='category'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('messages/', views.messages_view, name='messages'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

]
