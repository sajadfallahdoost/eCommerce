from django.contrib import admin
from warehouse.models.brand import Brand


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active', 'created', 'modified')
    search_fields = ('title', 'slug')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'modified')
