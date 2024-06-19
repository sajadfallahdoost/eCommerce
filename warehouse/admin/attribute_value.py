from django.contrib import admin
from warehouse.models import AttributeValue


@admin.register(AttributeValue)
class AttributeValueAdmin(admin.ModelAdmin):
    list_display = ('attval_title', 'parent', 'created', 'modified')
    search_fields = ('attval_title',)
    readonly_fields = ('created', 'modified')
