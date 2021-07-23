from django.db import models

# Create your models here.
class udefinlogin(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    gender=models.CharField(default="",max_length=20)
    email=models.CharField(max_length=30)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)
    postal_code=models.CharField(default="",max_length=100)
    location=models.CharField(max_length=10)
    address=models.CharField(max_length=30)