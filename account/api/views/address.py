from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import Address
from account.api.serializers import AddressSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
address_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'address_line_1': openapi.Schema(type=openapi.TYPE_STRING, description='Address Line 1'),
        'address_line_2': openapi.Schema(type=openapi.TYPE_STRING, description='Address Line 2', nullable=True),
        'city': openapi.Schema(type=openapi.TYPE_STRING, description='City'),
        'state': openapi.Schema(type=openapi.TYPE_STRING, description='State'),
        'zip_code': openapi.Schema(type=openapi.TYPE_STRING, description='ZIP Code'),
        'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country'),
        'corporate_profile': openapi.Schema(type=openapi.TYPE_INTEGER, description='Corporate Profile ID', nullable=True),
        'personal_profile': openapi.Schema(type=openapi.TYPE_INTEGER, description='Personal Profile ID', nullable=True)
    },
    required=['address_line_1', 'city', 'state', 'zip_code', 'country'],
    example={
        'address_line_1': '123 Main St',
        'address_line_2': 'Apt 4B',
        'city': 'New York',
        'state': 'NY',
        'zip_code': '10001',
        'country': 'USA',
        'corporate_profile': 1,
        'personal_profile': 1
    }
)

# Example for response body
address_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the address'),
        'address_line_1': openapi.Schema(type=openapi.TYPE_STRING, description='Address Line 1'),
        'address_line_2': openapi.Schema(type=openapi.TYPE_STRING, description='Address Line 2', nullable=True),
        'city': openapi.Schema(type=openapi.TYPE_STRING, description='City'),
        'state': openapi.Schema(type=openapi.TYPE_STRING, description='State'),
        'zip_code': openapi.Schema(type=openapi.TYPE_STRING, description='ZIP Code'),
        'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country'),
        'corporate_profile': openapi.Schema(type=openapi.TYPE_INTEGER, description='Corporate Profile ID', nullable=True),
        'personal_profile': openapi.Schema(type=openapi.TYPE_INTEGER, description='Personal Profile ID', nullable=True)
    },
    example={
        'id': 1,
        'address_line_1': '123 Main St',
        'address_line_2': 'Apt 4B',
        'city': 'New York',
        'state': 'NY',
        'zip_code': '10001',
        'country': 'USA',
        'corporate_profile': 1,
        'personal_profile': 1
    }
)

@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of addresses', AddressSerializer(many=True), examples={'application/json': [address_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=address_example,
    responses={
        201: openapi.Response('Address created', AddressSerializer, examples={'application/json': address_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
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

@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Address details', AddressSerializer, examples={'application/json': address_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=address_example,
    responses={
        200: openapi.Response('Address updated', AddressSerializer, examples={'application/json': address_response_example.example}),
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
