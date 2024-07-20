from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from config.swagger import schema_view


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', admin.site.urls),
    path('api/warehouse/', include('warehouse.api.urls')),
    path('api/shop/', include('shop.api.urls')),
    path('api/account/', include('account.api.urls')),
    path('api/otp/', include('services.otp.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
