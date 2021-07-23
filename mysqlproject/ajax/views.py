from django.shortcuts import render

# Create your views here.

def ajaxhome(request):
    return render(request, 'ajaxhome.html')

def jhome(request):
    return render(request, 'jqery_home.html')

def ajaxlogin(request):
    return render(request, 'ajaxlogin.html')

def ajaxregister(request):
    return render(request, 'ajaxregister.html')