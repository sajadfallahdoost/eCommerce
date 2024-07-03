from rest_framework import serializers
from shop.models import OrderAddress


class OrderAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAddress
        fields = ['country', 'province', 'city', 'postal_address', 'postal_code', 'house_number', 'building_unit', 'footnote', 'receiver_first_name', 'receiver_last_name', 'receiver_phone_number', 'receiver_national_code']
