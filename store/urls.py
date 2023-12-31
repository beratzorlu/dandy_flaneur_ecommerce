from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='store'),
    path('<int:product_id>/', views.store_detail, name='store_detail'),
    path('add_store/', views.add_store, name='add_store'),
    path('delete_store/<int:product_id>/', views.delete_store, name='delete_store'),
    path('edit_store/<int:product_id>/', views.edit_store, name='edit_store'),
]
