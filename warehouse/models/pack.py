from django.db import models
from django.utils.translation import gettext_lazy as _


from painless.models import StockUnitMixin, DescriptionMixin, TimestampMixin
from warehouse.models import Product, AttributeValue

# from warehouse.repository.manager.warehouse import (
#     WarehouseDateAccessLayer,
#     WarehouseBusinessLogicLayer
# )


class Pack(StockUnitMixin, DescriptionMixin, TimestampMixin):
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Price")
    )

    buy_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_("Buy Price")
    )

    stock = models.IntegerField(
        verbose_name=_("Stock")
    )

    actual_stock = models.IntegerField(
        verbose_name=_("Actual Stock")
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active")
    )

    is_default = models.BooleanField(
        default=False,
        verbose_name=_("Is Default")
    )

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='packs',
        verbose_name=_("Product")
    )

    att_val_ids = models.ManyToManyField(
        AttributeValue,
        blank=True,
        verbose_name=_("Attribute Values")
    )

    objects = models.Manager()
    # WarehouseDateAccessLayer = WarehouseDateAccessLayer()
    # WarehouseBusinessLogicLayer = WarehouseBusinessLogicLayer()

    class Meta:
        verbose_name = _("Pack")
        verbose_name_plural = _("Packs")
        db_table = 'warehouse_pack'
        ordering = ['sku']

    def __str__(self):
        return str(self.sku)
