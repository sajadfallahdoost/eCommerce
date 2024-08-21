from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from azbankgateways.urls import az_bank_gateways_urls
# from sep_payment.views import initiate_payment, verify_payment
from config.swagger import schema_view

admin.autodiscover()

urlpatterns = [
    path('admin/login/', csrf_exempt(admin.site.login)),
    path('admin/', admin.site.urls),
    path('api/warehouse/', include('warehouse.api.urls')),
    path('api/shop/', include('shop.api.urls')),
    path('api/account/', include('account.api.urls')),
    path('api/otp/', include('services.otp.api.urls')),
    path("api/payment/all_bank/", include('services.payment.payment_all_bank.api.urls')),
    path("api/payment/idpay/", include('services.payment.payment_idpay.api.urls')),
    path("api/payment/zarinpal/", include('services.payment.payment_zarinpal.api.urls')),
    path("api/payment/sep/", include('services.payment.payment_sep.api.urls')),
    path("bankgateways/", az_bank_gateways_urls(), name='bankgateways'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
