import os
import uuid

from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class TitleSlugMixin(models.Model):
    title = models.CharField(
        _("Title"),
        max_length=255,
        unique=True,
        null=True,
        help_text=_("The main textual identifier or name for the content"),
    )

    slug = models.SlugField(
        _("Slug"),
        max_length=255,
        unique=True,
        null=True,
        help_text=_(
            "A URL-friendly version of the title, typically used in"
            "the URL to identify the content's location."
        ),
    )

    class Meta:
        abstract = True


class SlugMixin(models.Model):
    slug = models.SlugField(
        _("Slug"),
        max_length=255,
        unique=True,
        help_text=_(
            "A URL-friendly version of the title, typically used in"
            "the URL to identify the content's location."
        ),
    )

    class Meta:
        abstract = True


class TimestampMixin(models.Model):
    created = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
        help_text=_(
            "The timestamp indicating when the model instance was"
            "initially added or created."
        ),
    )

    modified = models.DateTimeField(
        _("Modified at"),
        auto_now=True,
        help_text=_(
            "The timestamp representing the most recent update or"
            "modification to the model instance."
        ),
    )

    class Meta:
        abstract = True


class StockUnitMixin(models.Model):
    sku = models.UUIDField(
        _("Stock of Unit"),
        max_length=100,
        default=uuid.uuid4,
        unique=True,
        help_text=_("A unique identifier assigned to each product in inventory."),
    )

    class Meta:
        abstract = True


class DescriptionMixin(models.Model):
    description = models.TextField(
        _("Description"),
        null=True,
        blank=True,
        help_text=_(
            "A textual explanation or summary providing additional"
            "information about the item's characteristics or purpose."
        ),
    )

    class Meta:
        abstract = True


class PictureOperationAbstract(models.Model):
    alternate_text = models.CharField(
        _("Alternate Text"),
        max_length=110,
        validators=[MaxLengthValidator(150), MinLengthValidator(3)],
        null=True,
        blank=True,
        help_text=_(
            "Describe about picture that is uploaded. Please write a good description for search engines."
        ),
    )

    width_field = models.PositiveIntegerField(
        _("Picture Width"),
        null=True,
        blank=True,
        editable=False,
        help_text=_("size of picture's Width"),
    )

    height_field = models.PositiveIntegerField(
        _("Picture Height"),
        null=True,
        blank=True,
        editable=False,
        help_text=_("size of picture's Height"),
    )

    class Meta:
        abstract = True

    def get_picture_url(self):
        url = ""
        return self.picture.url if self.picture else "No Image"

    def get_picture_size(self):
        return self.picture.size

    def get_picture_dimensions(self):
        return (self.picture.width, self.picture.height)

    def get_file_name(self):
        return os.path.basename(self.picture.name)
