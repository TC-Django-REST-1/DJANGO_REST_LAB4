from django.db import models
from brand.models import brands
# Create your models here.
class products(models.Model):
    brand = models.ForeignKey(brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=512)
    description = models.TextField()
    image_url = models.URLField() 
    price = models.FloatField() 
    quantity = models.IntegerField(default=0) #
    is_active = models.BooleanField(default=False) #