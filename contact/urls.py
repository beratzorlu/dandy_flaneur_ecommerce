from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contactView.as_view(), name='contact')
]