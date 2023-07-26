from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('summernote/', include('django_summernote.urls')),
    path('add/', views.AddBlog.as_view(), name="blog_add"),
    path('<slug:slug>/delete', views.DeleteBlog.as_view(), name='blog_delete'),
    path('<slug:slug>/', views.PostDetail.as_view(), name="blog_detail"),
]
