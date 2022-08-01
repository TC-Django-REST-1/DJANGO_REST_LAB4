from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Brand(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    established_at = models.DateField()
    city = models.CharField(max_length=100, null=False)


class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    image_url = models.URLField(null=True)
    price = models.FloatField(null=False, validators=[MinValueValidator(0.0)])
    quantity = models.IntegerField(default=1, null=False)
    is_active = models.BooleanField(default=True)
