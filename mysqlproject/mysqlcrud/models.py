from django.db import models

# Create your models here.

class employee(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(default="",max_length=20)
    hobbies=models.CharField(default="",max_length=100)
    country=models.IntegerField(default=0)
    Employeestatus=models.TextChoices('Employeestatus','BLOCK UNBLOCK')
    status=models.CharField(default='BLOCK' ,choices=Employeestatus.choices,max_length=20)

class country(models.Model):
    country_name = models.CharField(default="", max_length=100)
