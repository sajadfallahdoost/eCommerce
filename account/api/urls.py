from django.urls import path
from rest_framework.routers import DefaultRouter

from account.api.views import (
    personal_profile_list_create,
    personal_profile_detail,
    corporate_profile_list_create,
    corporate_profile_detail,
    address_list_create,
    address_detail,
)

router = DefaultRouter()

urlpatterns = [
    path('personal-profiles/', personal_profile_list_create, name='personal-profile-list-create'),
    path('personal-profiles/<int:pk>/', personal_profile_detail, name='personal-profile-detail'),
    path('corporate-profiles/', corporate_profile_list_create, name='corporate-profile-list-create'),
    path('corporate-profiles/<int:pk>/', corporate_profile_detail, name='corporate-profile-detail'),
    path('addresses/', address_list_create, name='address-list-create'),
    path('addresses/<int:pk>/', address_detail, name='address-detail'),
]
