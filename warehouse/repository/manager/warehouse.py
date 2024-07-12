from django.db import models
from warehouse.repository.queryset.warehouse import WarehouseQuerySet
from warehouse.models import Product
from django.core.exceptions import ValidationError, ObjectDoesNotExist


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
        # checking for required fields
        required_fields = ['title', 'brand', 'category', 'sku']
        for field in required_fields:
            if field not in data:
                raise ValidationError(f"The field '{field}' is required.")

        if Product.objects.filter(title=data['title']).exists():
            raise ValidationError(f"A product with the title '{data['title']}' already exists.")

        product = Product.objects.create(**data)
        return product

    def update_product(self, product_id, data):
        try:
            # prevent updating the SKU if it exists
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            raise ValidationError(f"No product found with the ID '{product_id}'.")

        # prevent updating the SKU if it exists
        if 'sku' in data and Product.objects.filter(sku=data['sku']).exclude(id=product_id).exists():
            raise ValidationError(f"A product with the SKU '{data['sku']}' already exists.")

        for field, value in data.items():
            setattr(product, field, value)
        product.save()
        return product

    def delete_product(self, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except ObjectDoesNotExist:
            raise ValidationError(f"No product found with the ID '{product_id}'.")

        # prevent deletion if the product is associated with active orders
        if product.orders.exists():
            raise ValidationError("Cannot delete a product that is associated with active orders.")

        product.delete()
        return product
