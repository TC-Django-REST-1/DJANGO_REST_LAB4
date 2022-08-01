from rest_framework import serializers

from .models import Brand, Product


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'

    class Meta:
        model = Brand
        fields = '__all__'
