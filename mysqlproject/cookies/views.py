from django.shortcuts import render

# Create your views here.
def cookiehome(request):
    response=render(request,'setcooki.html')
    response.set_cookie('name','shriram',max_age=36000)
    return response

def getcookie(request):
    name=request.COOKIES.get('name','Guest')
    return render(request,'getcookie.html',{'name':name})

def delcookie(request):
    response = render(request, 'delcookie.html')
    response.delete_cookie('name')
    return response

def setsession(request):
    request.session['name']='shriram'
    return render(request,'setsession.html')

def getsession(request):
    #name=request.session['name']
    name=request.session.get('name',default='Guest')
    return render(request,'getsession.html',{'name':name})

def delsession(request):
    request.session.flush()
    return render(request,'delsession.html')