from rest_framework import serializers
from warehouse.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        extra_kwargs = {
            'url': {'lookup_field': 'slug'},
        }
