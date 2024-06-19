from django.contrib import admin
from warehouse.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_active',
                    'is_downloadable', 'parent', 'created', 'modified'
                    )
    search_fields = ('title', 'slug')
    list_filter = ('is_active', 'is_downloadable', 'parent')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created', 'modified')
