from django.urls import path, include
from rest_framework.routers import DefaultRouter
from shop.api.views import OrderViewSet, OrderAddressViewSet, CartViewSet, CartItemViewSet

router = DefaultRouter()

router.register(r'orders', OrderViewSet, basename="order")
router.register(r'order-addresses', OrderAddressViewSet, basename="orderaddress")
router.register(r'carts', CartViewSet, basename="cart")
router.register(r'cart-items', CartItemViewSet, basename="cartitem")

urlpatterns = [
    path('', include(router.urls)),
]
