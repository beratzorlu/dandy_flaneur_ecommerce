from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_basket, name='view_basket'),
    path('add_basket/<item_id>/', views.add_to_basket, name='add_to_basket'),
    path('edit_basket/<item_id>/', views.edit_basket, name='edit_basket'),
    path('remove_basket/<item_id>/', views.remove_basket, name='remove_basket'),
]
