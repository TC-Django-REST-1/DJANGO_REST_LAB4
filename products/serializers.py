from rest_framework.serializers import ModelSerializer
from .models import Brands, Products


class BrandsSerializer(ModelSerializer):
    class Meta:
        model = Brands
        fields = "__all__"


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
