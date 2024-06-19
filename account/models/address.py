from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models.corporateprofile import CorporateProfile
from account.models.personal_profile import PersonalProfile
from painless.models import TimestampMixin


class Address(TimestampMixin):
    address_line_1 = models.CharField(
        max_length=1024,
        verbose_name=_("Address Line 1")
    )

    address_line_2 = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        verbose_name=_("Address Line 2")
    )

    city = models.CharField(
        max_length=225,
        verbose_name=_("City")
    )

    state = models.CharField(
        max_length=225,
        verbose_name=_("State")
    )

    zip_code = models.CharField(
        max_length=225,
        verbose_name=_("ZIP Code")
    )

    country = models.CharField(
        max_length=225,
        verbose_name=_("Country")
    )

    corporate_profile = models.ForeignKey(
        CorporateProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Corporate Profile")
    )

    personal_profile = models.ForeignKey(
        PersonalProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("Personal Profile")
    )

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
        db_table = 'customer_address'
        ordering = ['city', 'state']

    def __str__(self):
        return f'{self.address_line_1}, {self.city}'
