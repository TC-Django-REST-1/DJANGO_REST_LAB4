from rest_framework import serializers
from .models import Brand, Product

class BrandSerializers(serializers.ModelSerializer):

    class Meta:
        model = Brand
        exclude = ['established_at']

class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ['image_url']


