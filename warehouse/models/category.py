from django.db import models
from django.utils.translation import gettext_lazy as _

from painless.models import TimestampMixin, TitleSlugMixin
from django.utils.text import slugify


class Category(TitleSlugMixin, TimestampMixin):
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active")
    )

    is_downloadable = models.BooleanField(
        default=False,
        verbose_name=_("Is Downloadable")
    )

    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name=_("Parent Category")
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        db_table = 'warehouse_category'
        ordering = ['title']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
