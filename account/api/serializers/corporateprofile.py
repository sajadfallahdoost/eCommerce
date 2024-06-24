from rest_framework import serializers
from account.models.corporateprofile import CorporateProfile


class CorporateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CorporateProfile
        fields = ['name', 'national_code', 'register_number', 'economical_code', 'phone']
