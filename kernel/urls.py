from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/warehouse', include('warehouse.api.urls')),
    path('api/shop', include('shop.api.urls')),
    path('api/account', include('account.api.urls')),
]
