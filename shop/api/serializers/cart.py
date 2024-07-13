from rest_framework import serializers
from shop.models.cart import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['user']
