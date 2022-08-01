from django.db import models

# Create your models here.
class brands(models.Model):
    title = models.CharField(max_length=512)
    description = models.TextField()
    established_at = models.DateTimeField()
    city = models.CharField(max_length=512)
