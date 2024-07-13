from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from shop.models.order_address import OrderAddress
from shop.api.serializers import OrderAddressSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
order_address_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country'),
        'province': openapi.Schema(type=openapi.TYPE_STRING, description='Province'),
        'city': openapi.Schema(type=openapi.TYPE_STRING, description='City'),
        'postal_address': openapi.Schema(type=openapi.TYPE_STRING, description='Postal address'),
        'postal_code': openapi.Schema(type=openapi.TYPE_STRING, description='Postal code'),
        'house_number': openapi.Schema(type=openapi.TYPE_INTEGER, description='House number'),
        'building_unit': openapi.Schema(type=openapi.TYPE_INTEGER, description='Building unit'),
        'footnote': openapi.Schema(type=openapi.TYPE_STRING, description='Footnote'),
        'receiver_first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Receiver first name'),
        'receiver_last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Receiver last name'),
        'receiver_phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Receiver phone number'),
        'receiver_national_code': openapi.Schema(type=openapi.TYPE_STRING, description='Receiver national code'),
    },
    required=['country', 'city', 'postal_address', 'receiver_first_name', 'receiver_last_name', 'receiver_phone_number', 'receiver_national_code'],
    example={
        'country': 'USA',
        'province': 'California',
        'city': 'San Francisco',
        'postal_address': '123 Market St',
        'postal_code': '94103',
        'house_number': 123,
        'building_unit': 45,
        'footnote': 'Leave at the front door',
        'receiver_first_name': 'John',
        'receiver_last_name': 'Doe',
        'receiver_phone_number': '1234567890',
        'receiver_national_code': '987654321',
    }
)

# Example for response body
order_address_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the order address'),
        'country': openapi.Schema(type=openapi.TYPE_STRING, description='Country'),
        'province': openapi.Schema(type=openapi.TYPE_STRING, description='Province'),
        'city': openapi.Schema(type=openapi.TYPE_STRING, description='City'),
        'postal_address': openapi.Schema(type=openapi.TYPE_STRING, description='Postal address'),
        'postal_code': openapi.Schema(type=openapi.TYPE_STRING, description='Postal code'),
        'house_number': openapi.Schema(type=openapi.TYPE_INTEGER, description='House number'),
        'building_unit': openapi.Schema(type=openapi.TYPE_INTEGER, description='Building unit'),
        'footnote': openapi.Schema(type=openapi.TYPE_STRING, description='Footnote'),
        'receiver_first_name': openapi.Schema(type=openapi.TYPE_STRING, description='Receiver first name'),
        'receiver_last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Receiver last name'),
        'receiver_phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='Receiver phone number'),
        'receiver_national_code': openapi.Schema(type=openapi.TYPE_STRING, description='Receiver national code'),
    },
    example={
        'id': 1,
        'country': 'USA',
        'province': 'California',
        'city': 'San Francisco',
        'postal_address': '123 Market St',
        'postal_code': '94103',
        'house_number': 123,
        'building_unit': 45,
        'footnote': 'Leave at the front door',
        'receiver_first_name': 'John',
        'receiver_last_name': 'Doe',
        'receiver_phone_number': '1234567890',
        'receiver_national_code': '987654321',
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of order addresses', OrderAddressSerializer(many=True), examples={'application/json': [order_address_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=order_address_example,
    responses={
        201: openapi.Response('Order address created', OrderAddressSerializer, examples={'application/json': order_address_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
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


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Order address details', OrderAddressSerializer, examples={'application/json': order_address_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=order_address_example,
    responses={
        200: openapi.Response('Order address updated', OrderAddressSerializer, examples={'application/json': order_address_response_example.example}),
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
