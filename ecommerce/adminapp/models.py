from django.db import models

# Create your models here.
class categorys(models.Model):
    category_name=models.CharField(max_length=100)
    Categorystatus = models.TextChoices('Categorystatus', 'BLOCK UNBLOCK')
    status = models.CharField(default='BLOCK', choices=Categorystatus.choices, max_length=20)


class subcategorys(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category=models.IntegerField(default=0)
    subcategorystatus = models.TextChoices('subcategorystatus', 'BLOCK UNBLOCK')
    status = models.CharField(default='BLOCK', choices=subcategorystatus.choices, max_length=20)

class Product(models.Model):
    category_ID = models.IntegerField(default=0)
    Subcategory_ID = models.IntegerField(default=0)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField(default=0)
    Discount = models.IntegerField(default=0)
    Discount_price = models.IntegerField(default=0)
    image =models.ImageField(upload_to="",null='True', blank='True')
    Descreption = models.CharField(max_length=100)
    productstatus = models.TextChoices('productstatus', 'BLOCK UNBLOCK')
    status = models.CharField(default='BLOCK', choices=productstatus.choices, max_length=20)