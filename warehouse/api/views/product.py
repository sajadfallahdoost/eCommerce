from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from warehouse.models import Product
from warehouse.api.serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body and response body
product_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Product title', example='New Product'),
        'subtitle': openapi.Schema(type=openapi.TYPE_STRING, description='Product subtitle', example='This is a new product'),
        'can_review': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Can review', example=True),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is active', example=True),
        'brand': openapi.Schema(type=openapi.TYPE_INTEGER, description='Brand ID', example=1),
        'category': openapi.Schema(type=openapi.TYPE_INTEGER, description='Category ID', example=1),
        'tags': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='Tag IDs', example=[1, 2]),
        'min_purchase': openapi.Schema(type=openapi.TYPE_INTEGER, description='Minimum purchase', example=1),
        'max_purchase': openapi.Schema(type=openapi.TYPE_INTEGER, description='Maximum purchase', example=10),
        'sku': openapi.Schema(type=openapi.TYPE_STRING, description='Stock Keeping Unit', example='123e4567-e89b-12d3-a456-426614174000'),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time')
    },
    required=['title', 'brand', 'category', 'sku']
)

# Example for response body
product_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the product'),
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Product title', example='New Product'),
        'slug': openapi.Schema(type=openapi.TYPE_STRING, description='Product slug', example='new-product'),
        'subtitle': openapi.Schema(type=openapi.TYPE_STRING, description='Product subtitle', example='This is a new product'),
        'can_review': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Can review', example=True),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is active', example=True),
        'brand': openapi.Schema(type=openapi.TYPE_INTEGER, description='Brand ID', example=1),
        'category': openapi.Schema(type=openapi.TYPE_INTEGER, description='Category ID', example=1),
        'tags': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='Tag IDs', example=[1, 2]),
        'min_purchase': openapi.Schema(type=openapi.TYPE_INTEGER, description='Minimum purchase', example=1),
        'max_purchase': openapi.Schema(type=openapi.TYPE_INTEGER, description='Maximum purchase', example=10),
        'sku': openapi.Schema(type=openapi.TYPE_STRING, description='Stock Keeping Unit', example='123e4567-e89b-12d3-a456-426614174000'),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time')
    },
    example={
        'id': 1,
        'title': 'New Product',
        'slug': 'new-product',
        'subtitle': 'This is a new product',
        'can_review': True,
        'is_active': True,
        'brand': 1,
        'category': 1,
        'tags': [1, 2],
        'min_purchase': 1,
        'max_purchase': 10,
        'sku': '123e4567-e89b-12d3-a456-426614174000',
        'created': '2023-06-22T18:25:43.511Z',
        'modified': '2023-06-22T18:25:43.511Z'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of products', ProductSerializer(many=True), examples={'application/json': [product_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=product_example,
    responses={
        201: openapi.Response('Product created', ProductSerializer, examples={'application/json': product_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def product_list_create(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Product details', ProductSerializer, examples={'application/json': product_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=product_example,
    responses={
        200: openapi.Response('Product updated', ProductSerializer, examples={'application/json': product_response_example.example}),
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
def product_detail(request, slug):
    """
    Retrieve, update or delete a product instance.
    """
    product = get_object_or_404(Product, slug=slug)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from warehouse.models import Product
# from warehouse.api.serializers import ProductSerializer


# class ProductViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductSerializer
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'slug'

#     def get_queryset(self):
#         return Product.objects.all()
