from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from warehouse.models import Pack
from warehouse.api.serializers import PackSerializer


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
