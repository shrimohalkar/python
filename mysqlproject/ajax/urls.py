from django.urls import path
from .import views

urlpatterns = [
    path('',views.ajaxhome,name='ajaxhome'),
    path('jhome',views.jhome,name="jhome"),
    path('ajaxlogin',views.ajaxlogin),
    path('ajaxregister',views.ajaxregister),
]