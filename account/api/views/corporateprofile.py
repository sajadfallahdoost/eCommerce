from rest_framework import viewsets
from account.models.corporateprofile import CorporateProfile
from account.api.serializers import CorporateProfileSerializer


class CorporateProfileViewSet(viewsets.ModelViewSet):
    serializer_class = CorporateProfileSerializer

    def get_queryset(self):
        return CorporateProfile.objects.all()
