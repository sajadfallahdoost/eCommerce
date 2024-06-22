from rest_framework import viewsets
from warehouse.models import Pack
from warehouse.api.serializers import PackSerializer


class PackViewSet(viewsets.ModelViewSet):
    serializer_class = PackSerializer
    lookup_field = 'sku'
    lookup_url_kwarg = 'sku'

    def get_queryset(self):
        return Pack.objects.all()
