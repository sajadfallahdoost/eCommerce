from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import TimestampMixin

# from warehouse.repository.manager.warehouse import (
#     WarehouseDateAccessLayer,
#     WarehouseBusinessLogicLayer
# )


class AttributeValue(TimestampMixin):
    attval_title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Attribute Value Title")
    )

    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_("Parent Attribute")
    )

    objects = models.Manager()
    # WarehouseDateAccessLayer = WarehouseDateAccessLayer()
    # WarehouseBusinessLogicLayer = WarehouseBusinessLogicLayer()

    class Meta:
        verbose_name = _("Attribute Value")
        verbose_name_plural = _("Attribute Values")
        db_table = 'warehouse_attribute_value'
        ordering = ['attval_title']

    def __str__(self):
        return self.attval_title
