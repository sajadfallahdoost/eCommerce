from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from shop.models import Cart
from shop.api.serializers import CartSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
cart_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID')
    },
    required=['user'],
    example={
        'user': 1
    }
)

# Example for response body
cart_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the cart'),
        'user': openapi.Schema(type=openapi.TYPE_INTEGER, description='User ID'),
    },
    example={
        'id': 1,
        'user': 1,
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of carts', CartSerializer(many=True), examples={'application/json': [cart_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=cart_example,
    responses={
        201: openapi.Response('Cart created', CartSerializer, examples={'application/json': cart_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['GET', 'POST'])
def cart_list_create(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Cart details', CartSerializer, examples={'application/json': cart_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=cart_example,
    responses={
        200: openapi.Response('Cart updated', CartSerializer, examples={'application/json': cart_response_example.example}),
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
def cart_detail(request, pk):
    cart = get_object_or_404(Cart, pk=pk)
    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from shop.models import Cart
# from shop.api.serializers import CartSerializer


# class CartViewSet(viewsets.ModelViewSet):
#     serializer_class = CartSerializer

#     def get_queryset(self):
#         return Cart.objects.all()
