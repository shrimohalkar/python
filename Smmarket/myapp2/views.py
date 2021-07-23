from django.shortcuts import render
from .models import student
from .forms import studentform
# Create your views here.

def student1(request):
    return render(request, 'student.html')

def adddata(request):
    #vname=request.GET['sname']
    #vname=request.POST['sname']
    vname=request.POST.get('sname')
    gender=request.POST.get('gender')
    country=request.POST.get('Country')
    language=request.POST.getlist('lang[]')

    return render(request,'result.html',{'stname':vname,'gender':gender,'country':country,'Language':language})


def showdata(request):
    obj=student.objects.all()
    return render(request, 'show.html',{'data':obj})


def stdform(request):
    obj1=studentform()
    return render(request, 'stdform.html', {'myform':obj1})
