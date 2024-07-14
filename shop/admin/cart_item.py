from django.contrib import admin
from shop.models.cart_item import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'pack', 'quantity', 'created', 'modified')
    search_fields = ('cart__user__username', 'pack__sku')
    readonly_fields = ('created', 'modified')
