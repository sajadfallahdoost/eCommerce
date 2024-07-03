from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from warehouse.models import Category
from warehouse.api.serializers import CategorySerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
category_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Category title'),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the category active?'),
        'is_downloadable': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the category downloadable?'),
        'parent': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the parent category (optional)'),
    },
    required=['title'],
    example={
        'title': 'Electronics',
        'is_active': True,
        'is_downloadable': False,
        'parent': None
    }
)

# Example for response body
category_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the category'),
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Category title'),
        'slug': openapi.Schema(type=openapi.TYPE_STRING, description='Category slug'),
        'is_active': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the category active?'),
        'is_downloadable': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Is the category downloadable?'),
        'parent': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the parent category (if any)'),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time')
    },
    example={
        'id': 1,
        'title': 'Electronics',
        'slug': 'electronics',
        'is_active': True,
        'is_downloadable': False,
        'parent': None,
        'created': '2023-06-22T18:25:43.511Z',
        'modified': '2023-06-22T18:25:43.511Z'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of categories', CategorySerializer(many=True), examples={'application/json': [category_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=category_example,
    responses={
        201: openapi.Response('Category created', CategorySerializer, examples={'application/json': category_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def category_list_create(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Category details', CategorySerializer, examples={'application/json': category_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=category_example,
    responses={
        200: openapi.Response('Category updated', CategorySerializer, examples={'application/json': category_response_example.example}),
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
def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from warehouse.models import Category
# from warehouse.api.serializers import CategorySerializer


# class CategoryViewSet(viewsets.ModelViewSet):
#     serializer_class = CategorySerializer
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'slug'

#     def get_queryset(self):
#         return Category.objects.all()
