from django.contrib import admin
from account.models.corporateprofile import CorporateProfile


@admin.register(CorporateProfile)
class CorporateProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'national_code',
                    'register_number', 'economical_code',
                    'phone', 'user', 'created', 'modified'
                    )
    search_fields = ('name', 'national_code', 'register_number', 'phone')
    readonly_fields = ('created', 'modified')
