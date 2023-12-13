from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Houses(models.Model):
    image1=models.ImageField(upload_to='images',blank=True,null=True)
    image2=models.ImageField(upload_to='images',blank=True,null=True)
    image3=models.ImageField(upload_to='images',blank=True,null=True)
    country=models.CharField(max_length=20,choices=[('india','india'),('china','china')],default='india')
    state=models.CharField(max_length=20,choices=[('karnataka','karnataka'),('haryana','haryana')],default='karnataka')
    district=models.CharField(max_length=20,choices=[('xyz','xyz'),('abc','abc')],default='udupi')
    address=models.CharField(max_length=50)
    housename=models.CharField(max_length=50,default="Royal")
    price=models.IntegerField(default=200)
    housetype=models.CharField(max_length=50,choices=[('1bhk','1bhk'),('2bhk','2bhk')],default="1bhk")
    contact=models.IntegerField(default=1234567891)
    desp=models.TextField(default="hello")
    createdby = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    issold=models.BooleanField(default=False)


class Result(models.Model):
    probuyer=models.CharField(max_length=50)
    proowner=models.CharField(max_length=50,default="yasir")

