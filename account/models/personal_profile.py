from django.db import models
from django.utils.translation import gettext_lazy as _
from account.models.user_profile import UserProfile


class PersonalProfile(UserProfile):
    first_name = models.CharField(
        max_length=1024,
        verbose_name=_("First Name")
    )

    last_name = models.CharField(
        max_length=1024,
        verbose_name=_("Last Name")
    )

    national_code = models.CharField(
        max_length=1024,
        unique=True,
        verbose_name=_("National Code")
    )

    gender = models.CharField(
        max_length=255,
        choices=[('male', _("Male")), ('female', _("Female"))],
        verbose_name=_("Gender")
    )

    phone = models.BigIntegerField(
        unique=True,
        verbose_name=_("Phone")
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=_("Birth Date")
    )

    job = models.CharField(
        max_length=1024,
        blank=True,
        null=True,
        verbose_name=_("Job")
    )

    class Meta:
        verbose_name = _("Personal Profile")
        verbose_name_plural = _("Personal Profiles")
        db_table = 'customer_perprofile'
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
