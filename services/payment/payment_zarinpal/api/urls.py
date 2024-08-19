from django.urls import path
from services.payment.payment_zarinpal.api.views import payment_zarinpal

urlpatterns = [
    path('payment_zarinpal/', payment_zarinpal, name='payment_zarinpal'),
]
