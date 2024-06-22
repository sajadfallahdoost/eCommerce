from rest_framework import viewsets
from warehouse.models import ProductGallery
from warehouse.api.serializers import ProductGallerySerializer


class ProductGalleryViewSet(viewsets.ModelViewSet):
    serializer_class = ProductGallerySerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return ProductGallery.objects.all()
