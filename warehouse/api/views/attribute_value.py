from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from warehouse.models.attribute_value import AttributeValue
from warehouse.api.serializers import AttributeValueSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
attribute_value_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'attval_title': openapi.Schema(type=openapi.TYPE_STRING, description='Attribute Value Title'),
        'parent': openapi.Schema(type=openapi.TYPE_INTEGER, description='Parent Attribute ID', nullable=True),
    },
    required=['attval_title'],
    example={
        'attval_title': 'Color',
        'parent': None,
    }
)

# Example for response body
attribute_value_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the attribute value'),
        'attval_title': openapi.Schema(type=openapi.TYPE_STRING, description='Attribute Value Title'),
        'parent': openapi.Schema(type=openapi.TYPE_INTEGER, description='Parent Attribute ID', nullable=True),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time')
    },
    example={
        'id': 1,
        'attval_title': 'Color',
        'parent': None,
        'created': '2023-06-22T18:25:43.511Z',
        'modified': '2023-06-22T18:25:43.511Z'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of attribute values', AttributeValueSerializer(many=True), examples={'application/json': [attribute_value_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=attribute_value_example,
    responses={
        201: openapi.Response('Attribute Value created', AttributeValueSerializer, examples={'application/json': attribute_value_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
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


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Attribute Value details', AttributeValueSerializer, examples={'application/json': attribute_value_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=attribute_value_example,
    responses={
        200: openapi.Response('Attribute Value updated', AttributeValueSerializer, examples={'application/json': attribute_value_response_example.example}),
        400: 'Bad Request - Invalid data',
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='delete',
    responses={
        204: 'No Content',
        404: 'Not Found'
    }
)
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
