"""mysqlproject URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mysqlcrud/',include('mysqlcrud.urls')),
    path('registerlogin/',include('registerlogin.urls')),
    path('cookies/',include('cookies.urls')),
    path('udefinlogin',include('udefinlogin.urls')),
    path('fileupload',include('fileupload.urls')),
    path('tempinheri',include('tempinheri.urls')),
    path('emailhandling', include('emailhandling.urls')),
    path('',include('ajax.urls')),
]
