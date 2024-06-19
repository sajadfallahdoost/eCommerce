from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from painless.models.common import TimestampMixin


class Cart(TimestampMixin):
    """
    Model representing a shopping cart.

    Attributes:
        user (User): The user to whom the cart belongs.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts', verbose_name=_("User"))

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")
        db_table = 'basket_cart'

    def __str__(self) -> str:
        return f'Cart {self.id} for {self.user.username}'
