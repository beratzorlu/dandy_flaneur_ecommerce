from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('summernote/', include('django_summernote.urls')),
    path('editor/', include('django_summernote.urls')),
    path('add/', views.AddBlog.as_view(), name="blog_add"),
    path('<slug:slug>/', views.PostDetail.as_view(), name="blog_detail"),
    path('<slug:slug>/delete', views.DeleteBlog.as_view(), name='blog_delete'),
    path('<slug:slug>/edit', views.EditBlog.as_view(), name='blog_edit'),
    path('<slug:slug>/like', views.LikeBlog.as_view(), name='blog_like'),
    path('comment/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
    path('comment/<int:comment_id>/edit/', views.comment_edit, name='comment_edit'),
]
