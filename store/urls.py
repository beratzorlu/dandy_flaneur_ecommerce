from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_list, name='store'),
    path('<int:product_id>/', views.store_detail, name='store_detail'),
]
