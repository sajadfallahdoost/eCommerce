from django.db import models
from django.utils.translation import gettext_lazy as _


from painless.models import TitleSlugMixin, TimestampMixin


class Category(TimestampMixin, TitleSlugMixin):
    description = models.TextField(
        null=True,
        blank=True,
        help_text=_("A brief description of the category, outlining its purpose or content.")
    )

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['title']
        db_table = 'blog_category'

    def __str__(self):
        return self.title
