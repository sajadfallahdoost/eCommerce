from rest_framework import serializers
from shop.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['transaction_number', 'total_price', 'status', 'order_address', 'user', 'cart']
