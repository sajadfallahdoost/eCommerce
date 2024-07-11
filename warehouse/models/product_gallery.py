from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models.common import PictureOperationAbstract, TimestampMixin, TitleSlugMixin
from warehouse.models import Product
from django.utils.text import slugify

# from warehouse.repository.manager.warehouse import (
#     WarehouseDateAccessLayer,
#     WarehouseBusinessLogicLayer
# )


class ProductGallery(PictureOperationAbstract, TimestampMixin, TitleSlugMixin):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='galleries',
        verbose_name=_("Product")
    )

    is_default = models.BooleanField(
        default=False,
        verbose_name=_("Is Default")
    )

    picture = models.ImageField(
        upload_to='media/uploads/product_pictures/',
        verbose_name=_("Picture")
    )

    objects = models.Manager()
    # WarehouseDateAccessLayer = WarehouseDateAccessLayer()
    # WarehouseBusinessLogicLayer = WarehouseBusinessLogicLayer()

    class Meta:
        verbose_name = _("Product Gallery")
        verbose_name_plural = _("Product Galleries")
        db_table = 'warehouse_product_gallery'
        ordering = ['product']

    def __str__(self):
        return f'{self.product.title} - {self.id}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
