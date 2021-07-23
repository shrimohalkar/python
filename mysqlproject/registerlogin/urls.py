from django.urls import path
from .import views

urlpatterns=[
    path('',views.registerfrom,name='register'),
    path('register',views.register,name='register'),
    path('login',views.loadlogin,name='login'),
    path('userlogin',views.userlogin, name='userlogin'),
    path('home',views.loadhome,name='home'),
    path('logout',views.userlogout, name='logout')
]