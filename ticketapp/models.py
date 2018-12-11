from django.db import models

# Create your models here.
class user(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    usersex = models.CharField(null=True, max_length=2)
    userpwd = models.CharField(max_length=20)

class picture(models.Model):
    picid = models.AutoField(primary_key=True)
    picpath = models.CharField(max_length=50)

class orderlist(models.Model):
    orderid = models.AutoField(primary_key=True)
    ordertime = models.CharField(max_length=20)

class ticket(models.Model):
    ticketid = models.AutoField(primary_key=True)
    ticketlocation = models.CharField(max_length=40)
    tickettime = models.CharField(max_length=20)
    ticketinfo = models.CharField(max_length=200)
    ticketprice = models.IntegerField()
    ticketstatus = models.IntegerField(default=0)

class address(models.Model):
    addrid = models.AutoField(primary_key=True)
    addrinfo = models.CharField(max_length=40)

class telephone(models.Model):
    teleid = models.AutoField(primary_key=True)
    teleinfo = models.CharField(max_length=40)