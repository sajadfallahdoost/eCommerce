from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from warehouse.models import ProductGallery
from warehouse.api.serializers import ProductGallerySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
product_gallery_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'product': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the associated product'),
        'is_default': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is this the default picture?'),
        'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY, description='Product picture')
    },
    required=['product', 'picture'],
    example={
        'product': 1,
        'is_default': True,
        'picture': 'image_data'
    }
)

# Example for response body
product_gallery_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the product gallery'),
        'product': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the associated product'),
        'is_default': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is this the default picture?'),
        'picture': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_BINARY, description='Product picture URL'),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time')
    },
    example={
        'id': 1,
        'product': 1,
        'is_default': True,
        'picture': 'url_to_image',
        'created': '2023-06-22T18:25:43.511Z',
        'modified': '2023-06-22T18:25:43.511Z'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of product galleries', ProductGallerySerializer(many=True), examples={'application/json': [product_gallery_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=product_gallery_example,
    responses={
        201: openapi.Response('Product gallery created', ProductGallerySerializer, examples={'application/json': product_gallery_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def product_gallery_list_create(request):
    if request.method == 'GET':
        product_galleries = ProductGallery.objects.all()
        serializer = ProductGallerySerializer(product_galleries, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductGallerySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Product gallery details', ProductGallerySerializer, examples={'application/json': product_gallery_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=product_gallery_example,
    responses={
        200: openapi.Response('Product gallery updated', ProductGallerySerializer, examples={'application/json': product_gallery_response_example.example}),
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
def product_gallery_detail(request, id):
    product_gallery = get_object_or_404(ProductGallery, id=id)
    if request.method == 'GET':
        serializer = ProductGallerySerializer(product_gallery)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductGallerySerializer(product_gallery, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        product_gallery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from warehouse.models import ProductGallery
# from warehouse.api.serializers import ProductGallerySerializer


# class ProductGalleryViewSet(viewsets.ModelViewSet):
#     serializer_class = ProductGallerySerializer
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'slug'

#     def get_queryset(self):
#         return ProductGallery.objects.all()
