from django.db import models

# Create your models here.

class employee(models.Model):

    Emp_name=models.CharField(max_length=20)
    Salary=models.IntegerField()
    Location=models.CharField(max_length=10)
