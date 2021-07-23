from django.contrib import admin
from django.urls import path
from.import views

urlpatterns=[
      #urlname  functionane   linkpages
     path('',views.employeepage, name='emphome'),
    path('reg',views.empfor,name='empform'),
    path('insertemp',views.insertemp, name='insertemp'),
    path('showemp',views.showemp, name='employeedetails'),
    path('delete/<int:eid>',views.deleteemp, name='deleteemp'),
    path('update/<int:eid>',views.updateemp, name='updateemp')
]