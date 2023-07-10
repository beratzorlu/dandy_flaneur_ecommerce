from django.urls import path
from . import views

urlpatterns = [
    path('', views.allWorkshops.as_view(), name='workshops'),
]
