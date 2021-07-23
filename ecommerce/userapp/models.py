from django.db import models

# Create your models here.

class signup(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    username=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    userstatus = models.TextChoices('userstatus', 'BLOCK UNBLOCK')
    status = models.CharField(default='BLOCK', choices=userstatus.choices, max_length=20)


