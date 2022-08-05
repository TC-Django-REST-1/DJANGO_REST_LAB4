from importlib.resources import read_binary
from rest_framework import serializers

from .models import Product, Brand


class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        exclude = ['id']


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
