from django.urls import path
from . import views

urlpatterns = [
    path('', views.profiles, name='profiles'),
    path('account_order_history/<order_number>', views.account_order_history,
         name='account_order_history'),
]
