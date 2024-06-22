from rest_framework import viewsets
from warehouse.models import Brand
from warehouse.api.serializers import BrandSerializer


class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return Brand.objects.all()
