from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User

# Create your models here.

class Brand(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    established_at = models.DateField(default=timezone.now)
    city = models.CharField(max_length=200)

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.ImageField(blank=True, upload_to=None)
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=False)
