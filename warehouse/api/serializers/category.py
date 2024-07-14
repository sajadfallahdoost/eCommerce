from rest_framework import serializers
from warehouse.models.category import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug', 'is_active', 'is_downloadable', 'parent']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }
