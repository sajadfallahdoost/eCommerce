from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import Address
from account.api.serializers import AddressSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def address_list_create(request):
    """
    List all addresses, or create a new address.
    """
    if request.method == 'GET':
        addresses = Address.objects.all()
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def address_detail(request, pk):
    """
    Retrieve, update or delete an address instance.
    """
    address = get_object_or_404(Address, pk=pk)

    if request.method == 'GET':
        serializer = AddressSerializer(address)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        address.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from rest_framework import viewsets
# from account.models import Address
# from account.api.serializers import AddressSerializer


# class AddressViewSet(viewsets.ModelViewSet):
#     serializer_class = AddressSerializer

#     def get_queryset(self):
#         return Address.objects.all()
