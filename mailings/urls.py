from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('clients/', views.ClientListView.as_view(), name='client-list'),
    path('clients/add/', views.ClientCreateView.as_view(), name='client-add'),
    path('clients/<int:pk>/edit/', views.ClientUpdateView.as_view(), name='client-edit'),
    path('clients/<int:pk>/delete/', views.ClientDeleteView.as_view(), name='client-delete'),
    path('messages/', views.MessageListView.as_view(), name='message-list'),
    path('messages/add/', views.MessageCreateView.as_view(), name='message-add'),
    path('messages/<int:pk>/edit/', views.MessageUpdateView.as_view(), name='message-edit'),
    path('messages/<int:pk>/delete/', views.MessageDeleteView.as_view(), name='message-delete'),
]