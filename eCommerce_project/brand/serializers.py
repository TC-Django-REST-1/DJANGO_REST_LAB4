from rest_framework.serializers import ModelSerializer
from .models import brands

class brandsSerializer(ModelSerializer):
    class Meta:
        model = brands
        fields = "__all__"