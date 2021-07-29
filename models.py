from django.db import models
from datetime import date
from Login.models import Login,Owner, Customer

class Coupon(models.Model):
    coup_id      = models.AutoField(primary_key=True)
    coup_name    = models.CharField(max_length=100)
    start_date   = models.DateField(default=date.today) 
    end_date     = models.DateField(default=date.today) 

    def __str__(self):
        return self.coup_name

class Get(models.Model):
    gid          = models.AutoField(primary_key=True)
    coup_id      = models.ForeignKey(Coupon,on_delete=models.CASCADE)
    username          = models.CharField(max_length=100,blank=True,null=True)
    coupon_unique_code = models.CharField(max_length=100,blank=True,null=True)
    status       = models.BooleanField(default=False)

    def __str__(self):
        return str(self.gid)+":"+self.username

class CouponHandling(models.Model):
    username    = models.CharField(primary_key=True,max_length=100)
    timestamp_login     = models.DateTimeField(blank=True,null=True)
    timestamp_logout    = models.DateTimeField(blank=True,null=True)
    total_usage = models.TimeField(blank=True,null=True)
    user    = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.username
        
class Vehicle(models.Model):
    vid          = models.AutoField(primary_key=True)
    vtype        = models.CharField(max_length=100)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return str(self.vid) + " : " + self.vtype

class Location(models.Model):
    locid        = models.AutoField(primary_key=True)
    ltype        = models.CharField(max_length=100)

    def __str__(self):
        return str(self.locid) + " : " + self.ltype

class View(models.Model):
    viewid        = models.AutoField(primary_key=True)
    locid         = models.ForeignKey(Location,on_delete=models.CASCADE)
    cid           = models.ForeignKey(Customer,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.viewid)