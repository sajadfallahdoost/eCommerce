from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from shop.models import CartItem
from shop.api.serializers import CartItemSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
cart_item_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'cart': openapi.Schema(type=openapi.TYPE_INTEGER, description='Cart ID'),
        'pack': openapi.Schema(type=openapi.TYPE_INTEGER, description='Pack ID'),
        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Quantity of the item')
    },
    required=['cart', 'pack', 'quantity'],
    example={
        'cart': 1,
        'pack': 2,
        'quantity': 3
    }
)

# Example for response body
cart_item_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the cart item'),
        'cart': openapi.Schema(type=openapi.TYPE_INTEGER, description='Cart ID'),
        'pack': openapi.Schema(type=openapi.TYPE_INTEGER, description='Pack ID'),
        'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description='Quantity of the item')
    },
    example={
        'id': 1,
        'cart': 1,
        'pack': 2,
        'quantity': 3
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of cart items', CartItemSerializer(many=True), examples={'application/json': [cart_item_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=cart_item_example,
    responses={
        201: openapi.Response('Cart item created', CartItemSerializer, examples={'application/json': cart_item_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def cart_item_list_create(request):
    if request.method == 'GET':
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Cart item details', CartItemSerializer, examples={'application/json': cart_item_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=cart_item_example,
    responses={
        200: openapi.Response('Cart item updated', CartItemSerializer, examples={'application/json': cart_item_response_example.example}),
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
def cart_item_detail(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk)
    if request.method == 'GET':
        serializer = CartItemSerializer(cart_item)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CartItemSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from shop.models import CartItem
# from shop.api.serializers import CartItemSerializer


# class CartItemViewSet(viewsets.ModelViewSet):
#     serializer_class = CartItemSerializer

#     def get_queryset(self):
#         return CartItem.objects.all()
