from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField()
    warehouse = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image_url', 'vendor', 'warehouse']

    def get_warehouse(self, obj):
        return obj.vendor.warehouse.name if obj.vendor and obj.vendor.warehouse else None