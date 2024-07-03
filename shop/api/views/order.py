from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from shop.models import Order
from shop.api.serializers import OrderSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
order_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'transaction_number': openapi.Schema(type=openapi.TYPE_STRING, description='Transaction number'),
        'total_price': openapi.Schema(type=openapi.TYPE_STRING, description='Total price'),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Status'),
        'order_address': openapi.Schema(type=openapi.TYPE_INTEGER, description='Order address ID'),
        'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
        'cart': openapi.Schema(type=openapi.TYPE_INTEGER, description='Cart ID'),
    },
    required=['transaction_number', 'total_price', 'status', 'order_address', 'user', 'cart'],
    example={
        'transaction_number': 'TX123456789',
        'total_price': '100.00',
        'status': 'submitted',
        'order_address': 1,
        'user': 1,
        'cart': 1,
    }
)

# Example for response body
order_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the order'),
        'transaction_number': openapi.Schema(type=openapi.TYPE_STRING, description='Transaction number'),
        'total_price': openapi.Schema(type=openapi.TYPE_STRING, description='Total price'),
        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Status'),
        'order_address': openapi.Schema(type=openapi.TYPE_INTEGER, description='Order address ID'),
        'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
        'cart': openapi.Schema(type=openapi.TYPE_INTEGER, description='Cart ID'),
        'created': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Creation time'),
        'modified': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Modification time'),
    },
    example={
        'id': 1,
        'transaction_number': 'TX123456789',
        'total_price': '100.00',
        'status': 'submitted',
        'order_address': 1,
        'user': 1,
        'cart': 1,
        'created': '2023-06-22T18:25:43.511Z',
        'modified': '2023-06-22T18:25:43.511Z'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of orders', OrderSerializer(many=True), examples={'application/json': [order_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=order_example,
    responses={
        201: openapi.Response('Order created', OrderSerializer, examples={'application/json': order_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def order_list_create(request):
    """
    List all orders, or create a new order.
    """
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Order details', OrderSerializer, examples={'application/json': order_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=order_example,
    responses={
        200: openapi.Response('Order updated', OrderSerializer, examples={'application/json': order_response_example.example}),
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
def order_detail(request, pk):
    """
    Retrieve, update or delete an order instance.
    """
    order = get_object_or_404(Order, pk=pk)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from shop.models import Order
# from shop.api.serializers import OrderSerializer


# class OrderViewSet(viewsets.ModelViewSet):
#     serializer_class = OrderSerializer

#     def get_queryset(self):
#         return Order.objects.all()
