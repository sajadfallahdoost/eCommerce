from django.contrib import admin
from warehouse.admin import ProductGalleryInline
from warehouse.models.product import Product
from warehouse.log.log import SingletonLogger

# Get the single logger instance
logger = SingletonLogger()


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

    # Override save_model to log product updates and creation
    def save_model(self, request, obj, form, change):
        if change:
            # Log product update
            logger.log(f"Admin {request.user.username} updated product '{obj.title}' (SKU: {obj.sku})")
        else:
            # Log product creation
            logger.log(f"Admin {request.user.username} added new product '{obj.title}' (SKU: {obj.sku})")
        super().save_model(request, obj, form, change)

    # Override delete_model to log product deletion
    def delete_model(self, request, obj):
        # Log product deletion
        logger.log(f"Admin {request.user.username} deleted product '{obj.title}' (SKU: {obj.sku})")
        super().delete_model(request, obj)
