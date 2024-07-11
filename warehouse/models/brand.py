from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from painless.models import TimestampMixin, TitleSlugMixin

# from warehouse.repository.manager.warehouse import (
#     WarehouseDateAccessLayer,
#     WarehouseBusinessLogicLayer
# )


class Brand(TimestampMixin, TitleSlugMixin):
    subtitle = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Subtitle")
    )

    picture = models.ImageField(
        upload_to='media/uploads/brand_pictures/',
        blank=True,
        null=True,
        verbose_name=_("Picture")
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active")
    )

    objects = models.Manager()
    # WarehouseDateAccessLayer = WarehouseDateAccessLayer()
    # WarehouseBusinessLogicLayer = WarehouseBusinessLogicLayer()

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")
        db_table = 'warehouse_brand'
        ordering = ['title']
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'slug'], name='unique_brand_title_slug')
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
