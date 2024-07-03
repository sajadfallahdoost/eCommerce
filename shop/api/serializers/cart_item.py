from rest_framework import serializers
from shop.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'pack', 'quantity']
