from rest_framework import viewsets
from warehouse.models import AttributeValue
from warehouse.api.serializers import AttributeValueSerializer


class AttributeValueViewSet(viewsets.ModelViewSet):
    serializer_class = AttributeValueSerializer
    lookup_field = 'attval_title'
    lookup_url_kwarg = 'attval_title'

    def get_queryset(self):
        return AttributeValue.objects.all()
