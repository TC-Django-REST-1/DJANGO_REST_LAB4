from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    established_at = models.PositiveIntegerField()
    city = models.CharField(max_length=255)

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=False)
