from django.urls import path
from .import views

urlpatterns = [
    path('',views.homeuser,name='userhome'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('insertuser',views.insertuser,name='insertuser'),
    path('uslogin',views.uslogin,name='uslogin'),
    path('ulogout',views.ulogout,name='ulogout'),
]