from django.contrib import admin
from account.models.address import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line_1', 'city', 'state', 'zip_code', 'country',
                    'corporate_profile', 'personal_profile',
                    'created', 'modified'
                    )
    search_fields = ('address_line_1', 'city', 'state', 'zip_code', 'country')
    readonly_fields = ('created', 'modified')
