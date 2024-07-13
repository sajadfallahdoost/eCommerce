from django.contrib import admin
from shop.models.order import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('transaction_number', 'total_price',
                    'status', 'order_address', 'user', 'created', 'modified'
                    )
    search_fields = (
        'transaction_number', 'user__username', 'order_address__city'
        )
    list_filter = ('status', 'created')
    readonly_fields = ('created', 'modified')
