from django.shortcuts import render,redirect
from .models import udefinlogin
from django.contrib import messages

# Create your views here.
def udhome(request):
    return render(request,'uhome.html')

def uabout(request):
    if ('user' in request.session):
        currentuser = request.session['user']
        return render(request,'about.html',{'currentuser': currentuser})
    else:
        return redirect('/udlogin')

def udsignupform(request):
    return render(request,'signup.html')

def udlogin(request):
    return render(request,'ulogin.html')

def insertrecord(request):
    if request.method=='POST':
        vufname=request.POST.get('ufname')
        vulname = request.POST.get('ulname')
        vuusername = request.POST.get('uusername')
        vugender=request.POST.get('gender')
        vuemail=request.POST.get('uemail')
        vumobile=request.POST.get('umobile')
        vupassword=request.POST.get('upassword')
        vupostal=request.POST.get('upostalcode')
        vulocation=request.POST.get('ulocation')
        vuaddress=request.POST.get('uaddress')

        ud = udefinlogin()
        ud.first_name=vufname
        ud.last_name=vulname
        ud.username=vuusername
        ud.gender=vugender
        ud.email=vuemail
        ud.mobile=vumobile
        ud.password=vupassword
        ud.postal_code=vupostal
        ud.location=vulocation
        ud.address=vuaddress
        ud.save()
        return redirect('udlogin')
    else:
        return render(request,'signup.html')

def uslogin(request):
    if request.method=='POST':
        vuusername=request.POST.get('username')
        vupassword=request.POST.get('password')

        user=udefinlogin.objects.filter(username=vuusername,password=vupassword).count()

        if(user==1):
            request.session['user']=vuusername  # set the session

            return redirect('/udshow')
        else:
            messages.info(request,"Invalid username & Password")
            return render(request,'ulogin.html')
    else:
        return render(request, 'ulogin.html')

def udshow(request):
    if('user' in request.session):
        currentuser=request.session['user']  # get the session
        ud = udefinlogin.objects.raw("select * from udefinlogin_udefinlogin where username='"+currentuser+"'")
        return render(request, 'udshow.html', {'currentuser': currentuser,'ud':ud})
    else:
        return redirect('/udlogin')

def ulogout(request):
    request.session.flush()
    return redirect('/udlogin')