from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    firstname = "Pune"
    return render(request,'uhome.html',{'name':firstname,'link':'profile','link1':'about'})

def profile(request):
    return render(request,'profile.html',{'tittles':'Shriram','link':'about'})

def about(request):
    return render(request,'about.html',{'tittles':'Shri','link':'/'})

def expresion(request):
    a=int(request.POST['1st'])
    b=int(request.POST['2nd'])
    c=a+b
    return render(request, 'output.html', {'result': c, 'home': '/'})
