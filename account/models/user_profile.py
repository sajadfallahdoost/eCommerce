from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from painless.models import TimestampMixin


class UserProfile(TimestampMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='%(class)s_profile',
        verbose_name=_("User")
    )

    class Meta:
        abstract = True
