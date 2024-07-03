from rest_framework import serializers
from account.models.personal_profile import PersonalProfile


class PersonalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProfile
        fields = ['first_name', 'last_name', 'national_code', 'gender', 'phone', 'birth_date', 'job']
