from django.db import models
from AdminApp.models import Mehandi
from datetime import datetime
# Create your models here.

class UserInfo(models.Model):
    
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    class Meta:
        db_table = "UserInfo"

class MyCart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    mehandi = models.ForeignKey(Mehandi,on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    
    class Meta:
        db_table = "MyCart"

class OrderMaster(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date_of_order = models.DateField(default = datetime.now)
    amount = models.FloatField(default=1000)
    details = models.CharField(max_length=200)
    

    class Meta:
        db_table = "OrderMaster"

class UserAppoinment(models.Model):
    emaill = models.CharField(max_length=20)
    usernamee = models.CharField(max_length=20,primary_key=True)
    phone = models.IntegerField(default = 10)
    date = models.DateField(default = datetime.now)
    message = models.CharField(max_length=100)

    class meta:
        db_table = "UserAppoinment"
        