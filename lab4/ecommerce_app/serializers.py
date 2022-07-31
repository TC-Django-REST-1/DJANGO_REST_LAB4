from dataclasses import Field, fields
from pyexpat import model
from rest_framework import serializers

from .models import Brand, Product

class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields ='__all__'

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
