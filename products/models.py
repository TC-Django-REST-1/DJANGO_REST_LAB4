from django.db import models
from django.core.validators import MinValueValidator


class Brands(models.Model):
    name = models.CharField(
        max_length=60, null=False, unique=True, help_text="Name of the brand"
    )
    description = models.CharField(
        max_length=255, null=False, help_text="Description of the brand"
    )
    established_at = models.DateTimeField(help_text="Established brand date")
    city = models.CharField(max_length=30, null=False, help_text="City of the brand")


class Products(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, null=False, help_text="Name of the product")
    description = models.CharField(
        max_length=255, null=False, help_text="Description of the product"
    )
    image_url = models.URLField(null=True, help_text="Image URL of the product")
    price = models.FloatField(
        null=False,
        validators=[MinValueValidator(0.0, message="Price must be bigger than 0.0")],
        help_text="Price of the product",
    )
    quantity = models.IntegerField(
        null=False, default=0, help_text="Quantity of the product"
    )
    is_active = models.BooleanField(
        default=False, help_text="Whether the product is active"
    )
