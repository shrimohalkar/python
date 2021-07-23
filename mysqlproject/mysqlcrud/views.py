from django.shortcuts import render, redirect
from .models import employee,country

# Create your views here.

def loademployeeFrom(request):
    cnt=country.objects.all()
    return render(request,'employee.html',{'country':cnt})

def insertrecord(request):
    if request.method=='POST':
        vname=request.POST.get('ename')
        vgender=request.POST.get('gender')
        vhobbies=request.POST.getlist('hobbies[]')
        vcountry=request.POST.get('cnt')
        emp=employee()
        emp.gender=vgender
        emp.hobbies=vhobbies
        emp.country=vcountry
        emp.name=vname # insert text box value to the column of emploee table
        emp.save()
        return redirect('/')
    else:
        return render(request,'employee.html')

def showemployee(request):
    # emp=employee.objects.all()
    emp=employee.objects.raw("select * from mysqlcrud_employee left join mysqlcrud_country on mysqlcrud_employee.country=mysqlcrud_country.id;")
    return render(request,'showemployee.html',{'emp':emp})

def deleterecord(request,eid):
    emp=employee.objects.get(id=eid)
    emp.delete()
    return redirect('show')

def editrecord(request,eid): # fetch the value in text box
    emp=employee.objects.get(id=eid)
    cntry=country.objects.all()
    return render(request,'editemployee.html',{'emp':emp, 'cntry':cntry})

def updaterecord(request,eid):
    emp=employee.objects.get(id=eid)
    vname= request.POST.get('ename')
    vhobbies = request.POST.getlist('hobbies[]')
    vcnt=request.POST.get('cnt')
    vgender = request.POST.get('gender')
    emp.name=vname
    emp.hobbies = vhobbies
    emp.country = vcnt
    emp.gender=vgender
    emp.save()
    return redirect('/show')

def employeestatus(request,eid,status):
    if(status=="BLOCK"):
        emp=employee.objects.get(id=eid)
        emp.status="UNBLOCK"
        emp.save()
        return redirect('/show')
    else:
        emp=employee.objects.get(id=eid)
        emp.status="BLOCK"
        emp.save()
        return redirect('/show')