from django.db import models

class Atributes(models.Model):
    caliber = models.CharField(max_length=100,blank=True)
    system = models.CharField(max_length=100,blank=True)
    capacity = models.CharField(max_length =100,blank=True)
    weight = models.CharField(max_length = 100,blank=True)
    length = models.CharField(max_length = 100,blank=True)
    material = models.CharField(max_length = 100,blank=True)
    operation=models.CharField(max_length = 100,blank=True)
    finishing = models.CharField(max_length = 100,blank=True) 
    model = models.CharField(max_length=100,blank=True)
   