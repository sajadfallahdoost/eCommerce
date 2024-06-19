from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from painless.models.common import TimestampMixin, TitleSlugMixin


class OrderAddress(TimestampMixin, TitleSlugMixin):
    """
    Model representing an order address.

    Attributes:
        country (str): The country of the address.
        province (str): The province of the address.
        city (str): The city of the address.
        postal_address (str): The postal address.
        postal_code (str): The postal code.
        house_number (str): The house number.
        building_unit (str): The building unit.
        footnote (str): Additional footnote.
        receiver_first_name (str): The first name of the receiver.
        receiver_last_name (str): The last name of the receiver.
        receiver_phone_number (str): The phone number of the receiver.
        receiver_national_code (str): The national code of the receiver.
    """

    country = models.CharField(max_length=255, verbose_name=_("Country"))
    province = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Province"))
    city = models.CharField(max_length=255, verbose_name=_("City"))
    postal_address = models.TextField(verbose_name=_("Postal Address"))
    postal_code = models.CharField(max_length=225, blank=True, null=True, verbose_name=_("Postal Code"))
    house_number = models.BigIntegerField(blank=True, null=True, verbose_name=_("House Number"))
    building_unit = models.BigIntegerField(blank=True, null=True, verbose_name=_("Building Unit"))
    footnote = models.TextField(blank=True, null=True, verbose_name=_("Footnote"))
    receiver_first_name = models.CharField(verbose_name=_("Receiver First Name"))
    receiver_last_name = models.CharField(verbose_name=_("Receiver Last Name"))
    receiver_phone_number = models.BigIntegerField(verbose_name=_("Receiver Phone Number"))
    receiver_national_code = models.BigIntegerField(verbose_name=_("Receiver National Code"))

    class Meta:
        verbose_name = _("Order Address")
        verbose_name_plural = _("Order Addresses")
        db_table = 'basket_orderaddresses'

    def __str__(self) -> str:
        return f'{self.receiver_first_name} {self.receiver_last_name}, {self.city}'

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)
