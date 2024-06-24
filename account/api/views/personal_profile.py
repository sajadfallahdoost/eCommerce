from rest_framework import viewsets
from account.models.personal_profile import PersonalProfile
from account.api.serializers import PersonalProfileSerializer


class PersonalProfileViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalProfileSerializer

    def get_queryset(self):
        return PersonalProfile.objects.all()
