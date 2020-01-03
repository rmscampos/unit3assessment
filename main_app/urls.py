from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('items/create/', views.ItemCreate.as_view(), name='items_create'),
  path('items/<int:pk>delete/', views.ItemDelete.as_view(), name='items_delete'),
]