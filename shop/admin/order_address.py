from django.contrib import admin
from shop.models.order_address import OrderAddress


@admin.register(OrderAddress)
class OrderAddressAdmin(admin.ModelAdmin):
    list_display = ('receiver_first_name', 'receiver_last_name',
                    'city', 'country', 'created', 'modified'
                    )
    search_fields = (
        'receiver_first_name', 'receiver_last_name', 'city', 'country')
    readonly_fields = ('created', 'modified')
