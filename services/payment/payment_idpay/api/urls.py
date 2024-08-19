from django.urls import path
from services.payment.payment_idpay.api.views import payment_idpay

urlpatterns = [
    path('payment_idpay/', payment_idpay, name='payment_idpay'),
]
