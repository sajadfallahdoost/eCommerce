from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from warehouse.models import Tag
from warehouse.api.serializers import TagSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
tag_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Tag title')
    },
    required=['title'],
    example={
        'title': 'Electronics'
    }
)

# Example for response body
tag_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the tag'),
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Tag title'),
        'slug': openapi.Schema(type=openapi.TYPE_STRING, description='Tag slug'),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time')
    },
    example={
        'id': 1,
        'title': 'Electronics',
        'slug': 'electronics',
        'created': '2023-06-22T18:25:43.511Z',
        'modified': '2023-06-22T18:25:43.511Z'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of tags', TagSerializer(many=True), examples={'application/json': [tag_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=tag_example,
    responses={
        201: openapi.Response('Tag created', TagSerializer, examples={'application/json': tag_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def tag_list_create(request):
    """
    List all tags, or create a new tag.
    """
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Tag details', TagSerializer, examples={'application/json': tag_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=tag_example,
    responses={
        200: openapi.Response('Tag updated', TagSerializer, examples={'application/json': tag_response_example.example}),
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
def tag_detail(request, slug):
    """
    Retrieve, update or delete a tag instance.
    """
    tag = get_object_or_404(Tag, slug=slug)

    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TagSerializer(tag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from warehouse.models import Tag
# from warehouse.api.serializers import TagSerializer


# class TagViewSet(viewsets.ModelViewSet):
#     serializer_class = TagSerializer
#     lookup_field = 'slug'
#     lookup_url_kwarg = 'slug'

#     def get_queryset(self):
#         return Tag.objects.all()
