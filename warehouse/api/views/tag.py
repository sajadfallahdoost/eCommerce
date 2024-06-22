from rest_framework import viewsets
from warehouse.models import Tag
from warehouse.api.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'slug'

    def get_queryset(self):
        return Tag.objects.all()
