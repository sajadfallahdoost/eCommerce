from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from painless.models import TimestampMixin, TitleSlugMixin
from django.db import models

# from warehouse.repository.manager.warehouse import (
#     WarehouseDateAccessLayer,
#     WarehouseBusinessLogicLayer
# )


class Tag(TimestampMixin, TitleSlugMixin):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")
        db_table = 'warehouse_tag'
        ordering = ['title']

    objects = models.Manager()
    # WarehouseDateAccessLayer = WarehouseDateAccessLayer()
    # WarehouseBusinessLogicLayer = WarehouseBusinessLogicLayer()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
