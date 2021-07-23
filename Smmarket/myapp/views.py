from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('Hello Django!!')

def home(request):
    name="John"
    m1=34
    m2=45
    m3=56
    list=[1,2,3,4,5,"ram","danny"]
    return render(request,'uhome.html',{'sname':name,'m1':m1,'m2':m2,'m3':m3,'mylist':list})
def about(request):
    name="pune"
    return render(request,'about.html',{'cityname':name})