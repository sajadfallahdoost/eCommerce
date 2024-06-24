from rest_framework import viewsets
from shop.models import Cart
from shop.api.serializers import CartSerializer


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.all()
