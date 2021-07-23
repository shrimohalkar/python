from django.urls import path
from .import views

urlpatterns=[
    path('',views.ihome,name='homei'),
    path('about', views.iabout, name='abouti'),
]