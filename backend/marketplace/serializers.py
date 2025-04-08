from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    vendor = serializers.StringRelatedField()
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image', 'vendor']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and hasattr(obj.image, 'url'):
            return request.build_absolute_uri(obj.image.url)
        return None
