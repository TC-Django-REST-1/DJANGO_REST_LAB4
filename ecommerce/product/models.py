from django.db import models
from statistics import mode

# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    established_at = models.DateField()
    city = models.CharField(max_length=512)


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    description = models.TextField()
    image_url = models.URLField()
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField()
    