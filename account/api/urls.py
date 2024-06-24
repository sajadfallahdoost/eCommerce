from django.urls import path, include
from rest_framework.routers import DefaultRouter
from account.api.views import CorporateProfileViewSet, PersonalProfileViewSet, AddressViewSet

router = DefaultRouter()

router.register(r'corporate-profiles', CorporateProfileViewSet, basename="corporateprofile")
router.register(r'personal-profiles', PersonalProfileViewSet, basename="personalprofile")
router.register(r'addresses', AddressViewSet, basename="address")

urlpatterns = [
    path('', include(router.urls)),
]
