from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import TitleSlugMixin, TimestampMixin, StockUnitMixin
from django.utils.text import slugify

# from warehouse.repository.manager.warehouse import (
#     WarehouseDateAccessLayer,
#     WarehouseBusinessLogicLayer
# )


class Product(TitleSlugMixin, TimestampMixin, StockUnitMixin):
    subtitle = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Subtitle")
    )

    can_review = models.BooleanField(
        default=False,
        verbose_name=_("Can Review")
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active")
    )

    suggested_products = models.ManyToManyField(
        'self',
        blank=True,
        # related_name='suggested_by',
        verbose_name=_("Suggested Products")
    )

    related_products = models.ManyToManyField(
        'self',
        blank=True,
        # related_name='related_by',
        verbose_name=_("Related Products")
    )

    brand = models.ForeignKey(
        'warehouse.Brand',
        on_delete=models.CASCADE,
        verbose_name=_("Brand")
    )

    category = models.ForeignKey(
        'warehouse.Category',
        on_delete=models.CASCADE,
        verbose_name=_("Category")
    )

    tags = models.ManyToManyField(
        'warehouse.Tag', blank=True,
        verbose_name=_("Tags")
    )

    min_purchase = models.IntegerField(
        default=1,
        verbose_name=_("Minimum Purchase")
    )

    max_purchase = models.IntegerField(
        default=1,
        verbose_name=_("Maximum Purchase")
    )

    objects = models.Manager()
    # WarehouseDateAccessLayer = WarehouseDateAccessLayer()
    # WarehouseBusinessLogicLayer = WarehouseBusinessLogicLayer()

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        db_table = 'warehouse_product'
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    # @property
    # def WarehouseDateAccessLayer(self):
    #     from repository.manager.warehouse import WarehouseDateAccessLayer
    #     return WarehouseDateAccessLayer()

    # @property
    # def WarehouseBusinessLogicLayer(self):
    #     from warehouse.repository.manager.warehouse import WarehouseBusinessLogicLayer
    #     return WarehouseBusinessLogicLayer()
