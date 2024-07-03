from rest_framework import serializers
from account.api.serializers.corporateprofile import CorporateProfileSerializer
from account.api.serializers.personal_profile import PersonalProfileSerializer
from account.models.corporateprofile import CorporateProfile
from account.models.personal_profile import PersonalProfile
from account.models import Address


class AddressSerializer(serializers.ModelSerializer):
    corporate_profile = CorporateProfileSerializer(read_only=True)
    personal_profile = PersonalProfileSerializer(read_only=True)

    class Meta:
        model = Address
        fields = ['address_line_1', 'address_line_2', 'city', 'state', 'zip_code', 'country', 'corporate_profile', 'personal_profile']