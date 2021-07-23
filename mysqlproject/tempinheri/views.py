from django.shortcuts import render, redirect

# Create your views here.
def ihome(request):
    return render(request,'homei.html')

def iabout(request):
    return render(request,'abouti.html')