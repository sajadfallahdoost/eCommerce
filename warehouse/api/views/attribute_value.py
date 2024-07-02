from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from warehouse.models import AttributeValue
from warehouse.api.serializers import AttributeValueSerializer


@api_view(['GET', 'POST'])
def attribute_value_list_create(request):
    if request.method == 'GET':
        attribute_values = AttributeValue.objects.all()
        serializer = AttributeValueSerializer(attribute_values, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AttributeValueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def attribute_value_detail(request, id):
    attribute_value = get_object_or_404(AttributeValue, id=id)
    if request.method == 'GET':
        serializer = AttributeValueSerializer(attribute_value)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AttributeValueSerializer(attribute_value, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        attribute_value.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from warehouse.models import AttributeValue
# from warehouse.api.serializers import AttributeValueSerializer


# class AttributeValueViewSet(viewsets.ModelViewSet):
#     serializer_class = AttributeValueSerializer
#     lookup_field = 'attval_title'
#     lookup_url_kwarg = 'attval_title'

#     def get_queryset(self):
#         return AttributeValue.objects.all()
