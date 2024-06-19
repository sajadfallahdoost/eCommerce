from django.contrib import admin
from warehouse.models import Pack


@admin.register(Pack)
class PackAdmin(admin.ModelAdmin):
    list_display = ('sku', 'price', 'buy_price', 'stock',
                    'actual_stock', 'is_active',
                    'is_default', 'product', 'created', 'modified'
                    )
    search_fields = ('sku', 'product__title')
    list_filter = ('is_active', 'is_default', 'product')
    readonly_fields = ('created', 'modified')
