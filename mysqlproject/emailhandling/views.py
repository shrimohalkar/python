from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from mysqlproject import settings # from project name setting

# Create your views here.

def mail(request):
    subject="Greetings"
    msg="Congratulations for your success"
    to=["krishna.itview@gmail.com","krish12shilong@gmail.com","mohalkar.ram@hotmail.com","deepali.dhere@gmail.com"]  #  mohalkar.ram@hotmail.com

    res= send_mail(subject,msg,settings.EMAIL_HOST_USER,to)

    if(res==1):
        msg="Mail sent successfully"
    else:
        msg="Mial could not sent"

    return HttpResponse(msg)

