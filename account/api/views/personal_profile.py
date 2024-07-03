from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import PersonalProfile
from account.api.serializers import PersonalProfileSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def personal_profile_list_create(request):
    """
    List all personal profiles, or create a new personal profile.
    """
    if request.method == 'GET':
        personal_profiles = PersonalProfile.objects.all()
        serializer = PersonalProfileSerializer(personal_profiles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonalProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def personal_profile_detail(request, pk):
    """
    Retrieve, update or delete a personal profile instance.
    """
    personal_profile = get_object_or_404(PersonalProfile, pk=pk)

    if request.method == 'GET':
        serializer = PersonalProfileSerializer(personal_profile)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonalProfileSerializer(personal_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        personal_profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework import viewsets
# from account.models.personal_profile import PersonalProfile
# from account.api.serializers import PersonalProfileSerializer


# class PersonalProfileViewSet(viewsets.ModelViewSet):
#     serializer_class = PersonalProfileSerializer

#     def get_queryset(self):
#         return PersonalProfile.objects.all()
