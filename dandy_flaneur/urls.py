"""dandy_flaneur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from .views import handler_404


@login_required
def redirect_admin(request):
    return redirect('/admin/blog/post/')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('redirect-admin/', redirect_admin, name='redirect_admin'),
    path('summernote/', include('django_summernote.urls')),
    path('editor/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('blog/', include('blog.urls')),
    path('', include('contact.urls')),
    path('store/', include('store.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'dandy_flaneur.views.handler_404'
handler500 = 'dandy_flaneur.views.handler_500'
