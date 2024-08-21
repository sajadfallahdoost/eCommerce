from django.urls import path
from services.payment.payment_sep.api.views import initiate_payment, verify_payment

urlpatterns = [
    path('initiate_payment', initiate_payment, name="initiate_payment"),
    path('verify_payment', verify_payment, name="verify_payment")
]
