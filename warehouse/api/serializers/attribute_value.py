from rest_framework import serializers
from warehouse.models.attribute_value import AttributeValue


class AttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValue
        fields = ['attval_title', 'parent']
        extra_kwargs = {
            'url': {'lookup_field': 'attval_title'},
        }
