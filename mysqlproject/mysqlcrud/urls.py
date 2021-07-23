from django.urls import path
from .import views

urlpatterns=[

    path('',views.loademployeeFrom,name='loadform'),
    path('insertrecord',views.insertrecord, name='insertrecord'),
    path('show/',views.showemployee,name='show'),
    path('delete/<int:eid>',views.deleterecord, name='delete'),
    path('edit/<int:eid>',views.editrecord, name='edit'),
    path('update/<int:eid>', views.updaterecord, name='update'),
    path('status/<int:eid>/<str:status>', views.employeestatus, name='status'),
]

