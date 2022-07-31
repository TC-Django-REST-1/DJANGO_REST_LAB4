from django.db import models

# Create your models here.

class Brand(models.Model):
    
    title = models.CharField(max_length=32, unique=True)
    description = models.TextField()
    established_at = models.DateTimeField(auto_now=True)
    city = models.CharField(max_length=128)