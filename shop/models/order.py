from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from painless.models.common import TimestampMixin
from shop.helper import TRANSACTION_STATUS


class Order(TimestampMixin):
    """
    Model representing an order.

    Attributes:
        transaction_number (str): The unique transaction number of the order.
        total_price (Decimal): The total price of the order.
        status (str): The status of the order.
        order_address (OrderAddress): The address associated with the order.
        user (User): The user who placed the order.
        cart (Cart): The cart associated with the order.
    """
    transaction_number = models.CharField(max_length=255, unique=True, verbose_name=_("Transaction Number"))
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Price"))
    status = models.CharField(max_length=50, choices=TRANSACTION_STATUS, default='submitted', verbose_name=_("Status"))
    order_address = models.ForeignKey('shop.OrderAddress', on_delete=models.CASCADE, verbose_name=_("Order Address"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name=_("User"))
    cart = models.ForeignKey('shop.Cart', on_delete=models.CASCADE, verbose_name=_("Cart"))

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")
        db_table = 'basket_orders'

    def __str__(self) -> str:
        return f'Order {self.id} - {self.transaction_number}'
