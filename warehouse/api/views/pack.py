from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from warehouse.models import Pack
from warehouse.api.serializers import PackSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
pack_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'sku': openapi.Schema(type=openapi.TYPE_STRING, format='uuid', description='Unique SKU identifier'),
        'price': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DECIMAL, description='Pack price'),
        'buy_price': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DECIMAL, description='Pack buy price'),
        'stock': openapi.Schema(type=openapi.TYPE_INTEGER, description='Stock quantity'),
        'actual_stock': openapi.Schema(type=openapi.TYPE_INTEGER, description='Actual stock quantity'),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the pack active?'),
        'is_default': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the pack default?'),
        'product': openapi.Schema(type=openapi.TYPE_INTEGER, description='Associated product ID'),
        'att_val_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='Attribute values'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='Pack description')
    },
    required=['price', 'buy_price', 'stock', 'actual_stock', 'product'],
    example={
        'sku': '123e4567-e89b-12d3-a456-426614174000',
        'price': 99.99,
        'buy_price': 79.99,
        'stock': 50,
        'actual_stock': 48,
        'is_active': True,
        'is_default': False,
        'product': 1,
        'att_val_ids': [1, 2, 3],
        'description': 'A detailed description of the pack'
    }
)

# Example for response body
pack_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the pack'),
        'sku': openapi.Schema(type=openapi.TYPE_STRING, format='uuid', description='Unique SKU identifier'),
        'price': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DECIMAL, description='Pack price'),
        'buy_price': openapi.Schema(type=openapi.TYPE_NUMBER, format=openapi.FORMAT_DECIMAL, description='Pack buy price'),
        'stock': openapi.Schema(type=openapi.TYPE_INTEGER, description='Stock quantity'),
        'actual_stock': openapi.Schema(type=openapi.TYPE_INTEGER, description='Actual stock quantity'),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the pack active?'),
        'is_default': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the pack default?'),
        'product': openapi.Schema(type=openapi.TYPE_INTEGER, description='Associated product ID'),
        'att_val_ids': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='Attribute values'),
        'description': openapi.Schema(type=openapi.TYPE_STRING, description='Pack description'),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time')
    },
    example={
        'id': 1,
        'sku': '123e4567-e89b-12d3-a456-426614174000',
        'price': 99.99,
        'buy_price': 79.99,
        'stock': 50,
        'actual_stock': 48,
        'is_active': True,
        'is_default': False,
        'product': 1,
        'att_val_ids': [1, 2, 3],
        'description': 'A detailed description of the pack',
        'created': '2023-06-22T18:25:43.511Z',
        'modified': '2023-06-22T18:25:43.511Z'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of packs', PackSerializer(many=True), examples={'application/json': [pack_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=pack_example,
    responses={
        201: openapi.Response('Pack created', PackSerializer, examples={'application/json': pack_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def pack_list_create(request):
    if request.method == 'GET':
        packs = Pack.objects.all()
        serializer = PackSerializer(packs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Pack details', PackSerializer, examples={'application/json': pack_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=pack_example,
    responses={
        200: openapi.Response('Pack updated', PackSerializer, examples={'application/json': pack_response_example.example}),
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
def pack_detail(request, id):
    pack = get_object_or_404(Pack, id=id)
    if request.method == 'GET':
        serializer = PackSerializer(pack)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PackSerializer(pack, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pack.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from warehouse.models import Pack
# from warehouse.api.serializers import PackSerializer


# class PackViewSet(viewsets.ModelViewSet):
#     serializer_class = PackSerializer
#     lookup_field = 'sku'
#     lookup_url_kwarg = 'sku'

#     def get_queryset(self):
#         return Pack.objects.all()
