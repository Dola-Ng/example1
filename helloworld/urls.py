"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.auth.views import login, logout
from login_1 import views as lviews
from happy import views as hviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('html.html/', views.index),
    path('', lviews.index_t),
    path('html/', views.index),
    path('login_t/', lviews.login_t),
    path('logout_t/', lviews.logout_t),
    path('register_t/', lviews.register_t),
    path('index_t/', lviews.index_t),
    path('homepage/', views.inyo),
    path('update/',views.update),
    path('homepage/update.html',views.update)
 
   
]




    


