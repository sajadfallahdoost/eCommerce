from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import CorporateProfile
from account.api.serializers import CorporateProfileSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def corporate_profile_list_create(request):
    """
    List all corporate profiles, or create a new corporate profile.
    """
    if request.method == 'GET':
        corporate_profiles = CorporateProfile.objects.all()
        serializer = CorporateProfileSerializer(corporate_profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CorporateProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def corporate_profile_detail(request, pk):
    """
    Retrieve, update or delete a corporate profile instance.
    """
    corporate_profile = get_object_or_404(CorporateProfile, pk=pk)

    if request.method == 'GET':
        serializer = CorporateProfileSerializer(corporate_profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CorporateProfileSerializer(corporate_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        corporate_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# from rest_framework import viewsets
# from account.models.corporateprofile import CorporateProfile
# from account.api.serializers import CorporateProfileSerializer


# class CorporateProfileViewSet(viewsets.ModelViewSet):
#     serializer_class = CorporateProfileSerializer

#     def get_queryset(self):
#         return CorporateProfile.objects.all()
