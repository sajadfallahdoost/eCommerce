from django.urls import path
from shop.api.views import (
    order_list_create,
    order_detail,
    order_address_list_create,
    order_address_detail,
    cart_list_create,
    cart_detail,
    cart_item_list_create,
    cart_item_detail,
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


urlpatterns = [
    path('orders/', order_list_create, name='order-list-create'),
    path('orders/<int:pk>/', order_detail, name='order-detail'),
    path('order-addresses/', order_address_list_create, name='order-address-list-create'),
    path('order-addresses/<int:pk>/', order_address_detail, name='order-address-detail'),
    path('carts/', cart_list_create, name='cart-list-create'),
    path('carts/<int:pk>/', cart_detail, name='cart-detail'),
    path('cart-items/', cart_item_list_create, name='cart-item-list-create'),
    path('cart-items/<int:pk>/', cart_item_detail, name='cart-item-detail'),
]


# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from shop.api.views import OrderViewSet, OrderAddressViewSet, CartViewSet, CartItemViewSet

# router = DefaultRouter()

# router.register(r'orders', OrderViewSet, basename="order")
# router.register(r'order-addresses', OrderAddressViewSet, basename="orderaddress")
# router.register(r'carts', CartViewSet, basename="cart")
# router.register(r'cart-items', CartItemViewSet, basename="cartitem")

# urlpatterns = [
#     path('', include(router.urls)),
# ]
