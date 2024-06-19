from django.contrib import admin
from warehouse.admin import ProductGalleryInline
from warehouse.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'sku', 'slug', 'brand', 'category', 'is_active',
                    'created', 'modified'
                    )
    search_fields = ('title', 'sku', 'slug')
    list_filter = ('is_active', 'brand', 'category', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductGalleryInline]
    readonly_fields = ('created', 'modified')
