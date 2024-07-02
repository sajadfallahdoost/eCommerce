from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from warehouse.models import ProductGallery
from warehouse.api.serializers import ProductGallerySerializer


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
