from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from warehouse.models import Brand
from warehouse.api.serializers import BrandSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
brand_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Brand title'),
        'subtitle': openapi.Schema(type=openapi.TYPE_STRING, description='Brand subtitle', nullable=True),
        'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY, description='Brand picture', nullable=True),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the brand active?', example=True),
    },
    required=['title'],
    example={
        'title': 'Nike',
        'subtitle': 'Just Do It',
        'picture': None,
        'is_active': True,
    }
)

# Example for response body
brand_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the brand'),
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Brand title'),
        'slug': openapi.Schema(type=openapi.TYPE_STRING, description='Brand slug'),
        'subtitle': openapi.Schema(type=openapi.TYPE_STRING, description='Brand subtitle', nullable=True),
        'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_URI, description='URL of the brand picture', nullable=True),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the brand active?'),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time'),
    },
    example={
        'id': 1,
        'title': 'Nike',
        'slug': 'nike',
        'subtitle': 'Just Do It',
        'picture': 'http://example.com/media/uploads/brand_pictures/nike.jpg',
        'is_active': True,
        'created': '2023-06-22T18:25:43.511Z',
        'modified': '2023-06-22T18:25:43.511Z'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of brands', BrandSerializer(many=True), examples={'application/json': [brand_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=brand_example,
    responses={
        201: openapi.Response('Brand created', BrandSerializer, examples={'application/json': brand_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def brand_list_create(request):
    if request.method == 'GET':
        brands = Brand.objects.all()
        serializer = BrandSerializer(brands, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = BrandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Brand details', BrandSerializer, examples={'application/json': brand_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=brand_example,
    responses={
        200: openapi.Response('Brand updated', BrandSerializer, examples={'application/json': brand_response_example.example}),
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
def brand_detail(request, id):
    brand = get_object_or_404(Brand, id=id)
    if request.method == 'GET':
        serializer = BrandSerializer(brand)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BrandSerializer(brand, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        brand.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from warehouse.models import Brand
# from warehouse.api.serializers import BrandSerializer


# class BrandViewSet(viewsets.ModelViewSet):
#     serializer_class = BrandSerializer
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'slug'

#     def get_queryset(self):
#         return Brand.objects.all()
