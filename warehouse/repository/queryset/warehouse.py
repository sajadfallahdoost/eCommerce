from django.db import models

from warehouse.models import (
    Product,
    ProductGallery,
    Pack,
    Brand,
    Category,
    AttributeValue
)


class WarehouseQuerySet(models.QuerySet):

    def get_products_by_category(category_id):
        return Product.objects.filter(category_id=category_id, is_active=True)

    def get_products_by_brand(brand_id):
        return Product.objects.filter(brand_id=brand_id, is_active=True)

    def search_products_by_title(keyword):
        return Product.objects.filter(title__icontains=keyword, is_active=True)

    def get_related_products(product):
        return product.related_products.filter(is_active=True)

    def get_suggested_products(product):
        return product.suggested_products.filter(is_active=True)

    def get_product_galleries(product_id):
        return ProductGallery.objects.filter(product_id=product_id)

    def get_packs_by_product(product_id):
        return Pack.objects.filter(product_id=product_id)

    def get_products_by_tag(tag_id):
        return Product.objects.filter(tags__id=tag_id, is_active=True)

    def get_subcategories(category_id):
        return Category.objects.filter(parent_id=category_id, is_active=True)

    def active(self):
        return self.filter(is_active=True)

    def by_category(self, category_id):
        return self.filter(category_id=category_id)

    def by_brand(self, brand_id):
        return self.filter(brand_id=brand_id)

    def search(self, query):
        return self.filter(title__icontains=query)

    active_products = Product.objects.filter(is_active=True)
    active_brands = Brand.objects.filter(is_active=True)
    active_packs = Pack.objects.filter(is_active=True)
    all_attribute_values = AttributeValue.objects.all()
