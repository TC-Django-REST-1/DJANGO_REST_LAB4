from django.db import models

# Create your models here.


class eCommerce_app(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    established_at = models.DateField()
    city = models.CharField(max_length=70)


class Product(models.Model):
    eCommerce_app = models.ForeignKey(eCommerce_app, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    image_url = models.URLField()
    price = models.FloatField()
    quantity = models.IntegerField()
    is_active = models.BooleanField()