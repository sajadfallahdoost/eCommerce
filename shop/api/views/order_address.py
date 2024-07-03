from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from shop.models import OrderAddress
from shop.api.serializers import OrderAddressSerializer


@api_view(['GET', 'POST'])
def order_address_list_create(request):
    if request.method == 'GET':
        order_addresses = OrderAddress.objects.all()
        serializer = OrderAddressSerializer(order_addresses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def order_address_detail(request, pk):
    order_address = get_object_or_404(OrderAddress, pk=pk)

    if request.method == 'GET':
        serializer = OrderAddressSerializer(order_address)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderAddressSerializer(order_address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order_address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from shop.models import OrderAddress
# from shop.api.serializers import OrderAddressSerializer


# class OrderAddressViewSet(viewsets.ModelViewSet):
#     serializer_class = OrderAddressSerializer

#     def get_queryset(self):
#         return OrderAddress.objects.all()
