from rest_framework import serializers
from warehouse.models import Brand


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['title', 'slug', 'subtitle', 'picture', 'is_active']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }
