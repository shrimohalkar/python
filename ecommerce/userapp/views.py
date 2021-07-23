from django.shortcuts import render,redirect
from .models import signup
from django.contrib import messages
from adminapp.models import categorys,subcategorys


# Create your views here.
def homeuser(request):
    cat=categorys.objects.all()
    scat=subcategorys.objects.all()
    return render(request,'userindex.html',{'cat':cat,'scat':scat})


def userlogin(request):
    return render(request,'userlogin.html')

def usersignup(request):
    return render(request,'usersignup.html')

def insertuser(request):
    if request.method=='POST':
        ufname = request.POST.get('fname')
        ulname = request.POST.get('lname')
        uemail = request.POST.get('uemail')
        uusername = request.POST.get('username')
        umobile = request.POST.get('mobile')
        upassword = request.POST.get('password')
        ucpassword = request.POST.get('confirm_password')

        if (upassword == ucpassword):
            sg=signup()
            sg.first_name=ufname
            sg.last_name=ulname
            sg.email=uemail
            sg.username=uusername
            sg.mobile=umobile
            sg.password=upassword
            sg.save()
            print("User Created")
            return redirect('/userlogin')
        else:
            messages.info(request,"Password not match")
            return redirect('/usersignup')

def uslogin(request):
    if request.method=='POST':
        uusername=request.POST.get('username')
        upassword=request.POST.get('password')

        user=signup.objects.filter(username=uusername,password=upassword).count()

        if(user==1):
            request.session['user']=uusername  # set the session
            return render(request,'userindex.html')
        else:
            messages.info(request,"Invalid username & Password")
            return render(request,'userlogin.html')
    else:
        return render(request, 'userlogin.html')

def ulogout(request):
    request.session.flush()
    return render(request,'userindex.html')