from rest_framework import viewsets
from shop.models import OrderAddress
from shop.api.serializers import OrderAddressSerializer


class OrderAddressViewSet(viewsets.ModelViewSet):
    serializer_class = OrderAddressSerializer

    def get_queryset(self):
        return OrderAddress.objects.all()
