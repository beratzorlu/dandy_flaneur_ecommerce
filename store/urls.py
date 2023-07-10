from django.urls import path
from . import views

urlpatterns = [
    path('', views.allProducts.as_view(), name='store'),
]