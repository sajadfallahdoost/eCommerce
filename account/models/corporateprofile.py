from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models.user_profile import UserProfile


class CorporateProfile(UserProfile):
    name = models.CharField(
        max_length=1024,
        verbose_name=_("Name")
    )

    national_code = models.BigIntegerField(
        unique=True,
        verbose_name=_("National Code")
    )

    register_number = models.BigIntegerField(
        unique=True,
        verbose_name=_("Register Number")
    )

    economical_code = models.BigIntegerField(
        blank=True,
        null=True,
        verbose_name=_("Economical Code")
    )

    phone = models.BigIntegerField(
        unique=True,
        verbose_name=_("Phone")
    )

    class Meta:
        verbose_name = _("Corporate Profile")
        verbose_name_plural = _("Corporate Profiles")
        db_table = 'customer_corprofile'
        ordering = ['name']

    def __str__(self):
        return self.name
