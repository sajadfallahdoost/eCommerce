from django.urls import path, include

from rest_framework.routers import DefaultRouter

from warehouse.api.views import (
    ProductViewSet, TagViewSet, ProductGalleryViewSet, PackViewSet,
    CategoryViewSet, BrandViewSet, AttributeValueViewSet
)
router = DefaultRouter()

router.register(r'products', ProductViewSet, basename="product")
router.register(r'tags', TagViewSet, basename="tag")
router.register(r'product-galleries', ProductGalleryViewSet, basename="productgallery")
router.register(r'packs', PackViewSet, basename="pack")
router.register(r'categories', CategoryViewSet, basename="category")
router.register(r'brands', BrandViewSet, basename="brand")
router.register(r'attribute-values', AttributeValueViewSet, basename="attributevalue")

urlpatterns = [
    path('', include(router.urls)),
]
