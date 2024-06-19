from django.contrib import admin
from warehouse.models import ProductGallery


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    readonly_fields = ('created', 'modified')
