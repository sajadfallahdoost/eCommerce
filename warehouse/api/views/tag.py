from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from warehouse.models import Tag
from warehouse.api.serializers import TagSerializer
from django.shortcuts import get_object_or_404


# @permission_classes([AllowAny])
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


# @permission_classes([AllowAny])
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
