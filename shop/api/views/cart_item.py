from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from shop.models import CartItem
from shop.api.serializers import CartItemSerializer


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
