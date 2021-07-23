from django.urls import path
from .import views

urlpatterns=[
    path('',views.udhome,name='udhome'),
    path('about', views.uabout, name='about'),
    path('udsignup',views.udsignupform,name='udsignup'),
    path('udlogin',views.udlogin,name='udlogin'),
    path('udinsertrecord',views.insertrecord,name='udinsertrecord'),
    path('udshow',views.udshow,name='udshow'),
    path('uslogin',views.uslogin,name='uslogin'),
    path('logout',views.ulogout,name='ulogout')

]