from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def registerfrom(request):
    return render(request,'register.html')

def register(request):
    if request.method=='POST':
        vfname=request.POST.get('fname')
        vlname = request.POST.get('lname')
        vusrname = request.POST.get('username')
        vemail = request.POST.get('email')
        vpassword = request.POST.get('password')
        vcpassword = request.POST.get('cpassword')

        if(vpassword==vcpassword):

            if(User.objects.filter(username=vusrname).exists()):
                messages.info(request,"Username already exists")
                return redirect('/')
            elif(User.objects.filter(email=vemail).exists()):
                messages.info(request, "email already exists")
                return redirect('/')

            newuser=User.objects.create_user(password=vpassword,first_name=vfname,last_name=vlname,username=vusrname,email=vemail)
            newuser.save()
            print("User Creted")
            return redirect('/')
        else:
            messages.info(request,"Password not match")
            return redirect('/')

    else:
        return render(request, 'register.html')


def loadlogin(request):
    return render(request, 'ulogin.html')

def userlogin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            vusername=request.POST.get('username')
            vpasswaord=request.POST.get('password')
            user=auth.authenticate(username=vusername,password=vpasswaord)
            if user is not None:
                auth.login(request,user) # login is predefined function
                return redirect('home')
            else:
                messages.info(request,'Invalid Credentials')
                return redirect('login')
        else:
            return render(request,'ulogin.html')
    else:
        return redirect('login')


def userlogout(request):
    auth.logout(request)
    return redirect('login')

def loadhome(request):
    if request.user.is_authenticated:
        return render(request, 'uhome.html')
    else:
        return redirect('login')