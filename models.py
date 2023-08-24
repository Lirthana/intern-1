from django.db import models


class CompanyName (models.Model):
    Address = models.CharField(max_length=100)
    PhoneNo = models.IntegerField(max_length=100)
    emailID = models.CharField(max_length=100)
    GSTIN = models.CharField(max_length=100)

class DeliveryChallanFor (models.Model):
    partyname = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    PhoneNo = models.IntegerField(max_length=100)
    EmailID = models.CharField(max_length=100)
    GSTIN =  models.CharField(max_length=100)

class ShippingTo (models.Model):
    shippingName = models.CharField(max_length=100) 
    Address = models.CharField(max_length=100)
    PhoneNo = models.IntegerField(max_length=100)
    EmailID = models.CharField(max_length=100)
    GSTIN =  models.CharField(max_length=100)  
    
