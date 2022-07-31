from django.db import models


class Brand(models.Model):
    #attributes 
    title = models.CharField(max_length=512)
    description = models.TextField()
    established_at = models.DateField()
    city = models.CharField(max_length=128)


class Product(models.Model):
    #attributes 
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    description = models.TextField()
    image_url = models.URLField()
    price =  models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField()