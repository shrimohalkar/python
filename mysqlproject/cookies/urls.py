from django.urls import path
from .import views

urlpatterns = [
    path('',views.cookiehome,name='setcookie'),
    path('get',views.getcookie,name='getcookie'),
    path('del',views.delcookie,name='delcokkie'),
    path('sets',views.setsession,name='setsession'),
    path('gets',views.getsession,name='getsession'),
    path('dels',views.delsession,name='delsession'),
]