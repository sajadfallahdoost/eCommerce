from django.db import models
from django.utils.translation import gettext_lazy as _
from painless.models.common import TimestampMixin
from warehouse.models.pack import Pack
from shop.models.cart import Cart


class CartItem(TimestampMixin):
    """
    Model representing an item in a shopping cart.

    Attributes:
        cart (Cart): The cart to which the item belongs.
        pack (Pack): The pack associated with the item.
        quantity (int): The quantity of the item.
    """

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name=_("Cart"))
    pack = models.ForeignKey(Pack, on_delete=models.CASCADE, related_name='cart_items', verbose_name=_("Pack"))
    quantity = models.BigIntegerField(verbose_name=_("Quantity"))

    class Meta:
        verbose_name = _("Cart Item")
        verbose_name_plural = _("Cart Items")
        db_table = 'basket_cartitem'

    def __str__(self) -> str:
        return f'{self.quantity} x {self.pack.sku}'
