from rest_framework import serializers
from shop.models.cart_item import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cart', 'pack', 'quantity']
