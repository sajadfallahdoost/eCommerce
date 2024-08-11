from django.urls import path
from services.payment.api.views import go_to_gateway_view, payment_request

urlpatterns = [
    path('go_to_gateway_view/', go_to_gateway_view, name='go_to_gateway_view'),
    path('payment_request/', payment_request, name='payment_zarinpal_test'),
]
