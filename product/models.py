from ast import mod
from django.db import models
from brand.models import Brand
# Create your models here.

class Product(models.Model):

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    description = models.TextField()
    image_url = models.URLField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)