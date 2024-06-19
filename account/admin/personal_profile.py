from django.contrib import admin
from account.models.personal_profile import PersonalProfile


@admin.register(PersonalProfile)
class PersonalProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'national_code',
                    'gender', 'phone', 'birth_date', 'job',
                    'user', 'created', 'modified'
                    )
    search_fields = ('first_name', 'last_name', 'national_code', 'phone')
    list_filter = ('gender', 'birth_date')
    readonly_fields = ('created', 'modified')
