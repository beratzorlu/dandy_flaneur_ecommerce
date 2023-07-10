from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogList.as_view(), name='blog')
]