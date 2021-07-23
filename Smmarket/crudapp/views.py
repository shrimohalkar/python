from django.shortcuts import render,redirect
from .models import employee
from .forms import empform

# Create your views here.

def employeepage(request):
 return render(request, 'mycrud.html')

def empfor(request):
  emp=empform()
  return render(request, 'regform.html', {'regform':emp})

# insert value into

def insertemp(request):
    if request.method =='POST':
        employeeform=empform(request.POST)
        if(employeeform.is_valid()):
            employeeform.save()
    return redirect('/showemp')


def showemp(request):
    empdata=employee.objects.all()
    return render(request,'showemp.html',{'empdetails':empdata})

def deleteemp(request, eid):
    emp=employee.objects.get(id=eid)
    emp.delete()
    return redirect('/showemp')

def updateemp(request,eid):
    if request.method=='POST':
        emp=employee.objects.get(id=eid)
        frm=empform(request.POST, instance=emp)
        if(frm.is_valid()):
            frm.save()
            return redirect('/showemp')
    else:
        emp=employee.objects.get(id=eid)
        frm=empform(instance=emp)
        return render(request, 'editemp.html',{'form':frm})
