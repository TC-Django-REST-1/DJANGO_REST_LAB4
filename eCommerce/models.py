from enum import unique
from django.db import models

# Create your models here.


class Brand(models.Model):
    title = models.CharField(max_length=512, primary_key=True)
    description = models.TextField()
    established_at = models.DateField()
    city = models.CharField(max_length=40)


class Product(models.Model):
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='name')
    name = models.CharField(max_length=128)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=3)
    quantity = models.PositiveIntegerField()
    is_active = models.BooleanField()

    class Meta:
        unique_together = (('brand', 'name'),)
