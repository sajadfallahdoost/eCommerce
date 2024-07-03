from django.urls import path
from warehouse.api.views import (
    product_list_create,
    product_detail,
    tag_list_create,
    tag_detail,
    product_gallery_list_create,
    product_gallery_detail,
    pack_list_create,
    pack_detail,
    category_list_create,
    category_detail,
    brand_list_create,
    brand_detail,
    attribute_value_list_create,
    attribute_value_detail,
)


urlpatterns = [
    path('products/', product_list_create, name='product-list-create'),
    path('products/<slug:slug>/', product_detail, name='product-detail'),
    path('tags/', tag_list_create, name='tag-list-create'),
    path('tags/<int:id>/', tag_detail, name='tag-detail'),
    path('product-galleries/', product_gallery_list_create, name='product-gallery-list-create'),
    path('product-galleries/<int:id>/', product_gallery_detail, name='product-gallery-detail'),
    path('packs/', pack_list_create, name='pack-list-create'),
    path('packs/<int:id>/', pack_detail, name='pack-detail'),
    path('categories/', category_list_create, name='category-list-create'),
    path('categories/<int:id>/', category_detail, name='category-detail'),
    path('brands/', brand_list_create, name='brand-list-create'),
    path('brands/<int:id>/', brand_detail, name='brand-detail'),
    path('attribute-values/', attribute_value_list_create, name='attribute-value-list-create'),
    path('attribute-values/<int:id>/', attribute_value_detail, name='attribute-value-detail'),
]


# from django.urls import path, include

# from rest_framework.routers import DefaultRouter

# from warehouse.api.views import (
#     ProductViewSet, TagViewSet, ProductGalleryViewSet, PackViewSet,
#     CategoryViewSet, BrandViewSet, AttributeValueViewSet
# )
# router = DefaultRouter()


# router.register(r'products', ProductViewSet, basename="product")
# router.register(r'tags', TagViewSet, basename="tag")
# router.register(r'product-galleries', ProductGalleryViewSet, basename="productgallery")
# router.register(r'packs', PackViewSet, basename="pack")
# router.register(r'categories', CategoryViewSet, basename="category")
# router.register(r'brands', BrandViewSet, basename="brand")
# router.register(r'attribute-values', AttributeValueViewSet, basename="attributevalue")

# urlpatterns = [
#     path('', include(router.urls)),
# ]
