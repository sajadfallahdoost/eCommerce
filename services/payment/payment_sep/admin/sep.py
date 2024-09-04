from django.contrib import admin
from services.payment.payment_sep.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('res_num', 'terminal_id', 'amount', 'status', 'created_at', 'updated_at')
