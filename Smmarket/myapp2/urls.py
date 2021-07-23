from django.contrib import admin
from django.urls import path
from.import views

urlpatterns=[
      #urlname  functionane   linkpages
    path('',views.student1,name='studentpage'),
    path('adddata',views.adddata, name='adddata'),
    path('show',views.showdata, name='show'),
    path('load', views.stdform, name='loadfrom')
]