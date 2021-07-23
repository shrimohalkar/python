from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.login,name='login'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('logout',views.logout,name='logout'),
    path('category',views.category,name='category'),
    path('product',views.product,name='product'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('insertproduct',views.insertproduct,name='insertproduct'),
    path('deleteproduct/<int:eid>',views.deleteproduct,name='deleteproduct'),
    path('subcategory',views.subcategory,name='subcategory'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addsubcategory',views.addsubcategory,name='addsubcategory'),
    path('insertrecord',views.insertrecord,name='insertrecord'),
    path('insertsubcat',views.insertsubcat,name='insertsubcat'),
    path('delete/<int:eid>',views.deleterecord,name='delete'),
    path('delete_manage_user/<int:eid>',views.delete_manage_user,name='delete_manage_user'),
    path('deletesubcategory/<int:eid>',views.deletesubcat,name='deletesubcategory'),
    path('edit/<int:eid>',views.editcategory,name='edit'),
    path('editproduct/<int:eid>',views.editproduct,name='editproduct'),
    path('editsubcat/<int:eid>',views.editsubcat,name='editsubcat'),
    path('update/<int:eid>',views.updatecategory,name='update'),
    path('updateproduct/<int:eid>',views.updateproduct,name='updateproduct'),
    path('updatesubcategory/<int:eid>',views.updatesubcategory,name='updatesubcategory'),
    path('status/<int:eid>/<str:status>', views.categorystatus, name='status'),
    path('substatus/<int:eid>/<str:status>', views.subcategorystatus, name='status'),
    path('productstatus/<int:eid>/<str:status>', views.productstatus, name='productstatus'),
    path('userstatus/<int:eid>/<str:status>', views.userstatus, name='userstatus'),
    path('getsubcategory',views.getsubcategory,name='getsubcategory'),
    path('manage_user',views.manage_user,name='manage_user'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)