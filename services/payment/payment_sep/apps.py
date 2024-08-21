from django.apps import AppConfig


class PaymentSepConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "services.payment.payment_sep"
    label = "payment_sep"
