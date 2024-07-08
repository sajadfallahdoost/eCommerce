from django.db import models
from warehouse.repository.queryset.warehouse import WarehouseQuerySet
from warehouse.models import Product


class WarehouseDateAccessLayer(models.Manager):
    def get_queryset(self):
        return WarehouseQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def by_category(self, category_id):
        return self.get_queryset().by_category(category_id)

    def by_brand(self, brand_id):
        return self.get_queryset().by_brand(brand_id)

    def search(self, query):
        return self.get_queryset().search(query)


class WarehouseBusinessLogicLayer(models.Manager):
    """
    Handles functions affecting the warehouse.
    """
    def create_product(self, data):
        product = Product.objects.create(**data)
        return product

    def update_product(self, product_id, data):
        product = Product.objects.get(id=product_id)
        for field, value in data.items():
            setattr(product, field, value)
        product.save()
        return product

    def delete_product(self, product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return product
