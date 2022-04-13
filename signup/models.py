from django.db import models

# Create your models here.

class signup(models.Model):
    username=models.CharField(max_length=15, primary_key=True)
    password=models.CharField(max_length=100)
    phoneno=models.BigIntegerField(max_length=10)
    city=models.CharField(max_length=20)
    som=models.DecimalField(max_digits=14,decimal_places=2, default=0)

class stocks(models.Model):
    symbol=models.CharField(max_length=20, primary_key=True)
    name=models.CharField(max_length=23)
    last=models.DecimalField(max_digits=8, decimal_places=2,default=0)
    change=models.DecimalField(max_digits=6, decimal_places=2,default=0)
    change_percentage=models.DecimalField(max_digits=6, decimal_places=2,default=0)


class transaction(models.Model):
    t_id=models.AutoField(primary_key=True)
    buyer=models.CharField(max_length=15)
    seller=models.CharField(max_length=15)
    stock=models.CharField(max_length=25)
    amount=models.IntegerField(10000)
    status=models.CharField(max_length=1)
    shares=models.IntegerField(1000)
