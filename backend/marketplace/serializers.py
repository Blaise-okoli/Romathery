from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image_url', 'vendor']