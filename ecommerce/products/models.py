from pyexpat import model
from tkinter import CASCADE
from turtle import title
from django.db import models

# Create your models here.
# Brand:title description established_at  city

class Brand(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    established_at=models.DateField()
    city=models.CharField(max_length=200)


#  Product: brand name description image_url price quantity is_active

class Product(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description =  models.TextField()
    image_url = models.URLField()
    price =models.FloatField()
    quantity=models.IntegerField() 
    is_active=models.BooleanField()