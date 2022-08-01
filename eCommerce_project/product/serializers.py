from rest_framework.serializers import ModelSerializer
from .models import products

class productsSerializer(ModelSerializer):
    class Meta:
        model = products
        fields = "__all__"