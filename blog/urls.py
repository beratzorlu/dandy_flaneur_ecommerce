from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('summernote/', include('django_summernote.urls')),
    path('<slug:slug>/', views.PostDetail.as_view(), name="blog_detail")
]
