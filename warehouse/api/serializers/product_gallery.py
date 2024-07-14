from rest_framework import serializers
from warehouse.models.product_gallery import ProductGallery


class ProductGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductGallery
        fields = ['product', 'is_default', 'picture']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }
