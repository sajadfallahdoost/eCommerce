from django.contrib import admin
from shop.models.cart import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'modified')
    search_fields = ('user__username',)
    readonly_fields = ('created', 'modified')
