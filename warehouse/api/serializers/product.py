from rest_framework import serializers
from warehouse.models.product import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title', 'slug', 'subtitle', 'can_review', 'is_active', 'suggested_products',
            'related_products', 'brand', 'category', 'tags', 'min_purchase', 'max_purchase'
        ]
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }
