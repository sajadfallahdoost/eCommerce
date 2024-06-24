from rest_framework import viewsets
from shop.models import CartItem
from shop.api.serializers import CartItemSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.all()
