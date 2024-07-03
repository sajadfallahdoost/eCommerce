from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import PersonalProfile
from account.api.serializers import PersonalProfileSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
personal_profile_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
        'national_code': openapi.Schema(type=openapi.TYPE_STRING, description='National Code'),
        'gender': openapi.Schema(type=openapi.TYPE_STRING, enum=['male', 'female'], description='Gender'),
        'phone': openapi.Schema(type=openapi.TYPE_INTEGER, description='Phone'),
        'birth_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Birth Date'),
        'job': openapi.Schema(type=openapi.TYPE_STRING, description='Job')
    },
    required=['first_name', 'last_name', 'national_code', 'gender', 'phone'],
    example={
        'first_name': 'John',
        'last_name': 'Doe',
        'national_code': '1234567890',
        'gender': 'male',
        'phone': 1234567890,
        'birth_date': '2000-01-01',
        'job': 'Developer'
    }
)

# Example for response body
personal_profile_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the personal profile'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name'),
        'national_code': openapi.Schema(type=openapi.TYPE_STRING, description='National Code'),
        'gender': openapi.Schema(type=openapi.TYPE_STRING, enum=['male', 'female'], description='Gender'),
        'phone': openapi.Schema(type=openapi.TYPE_INTEGER, description='Phone'),
        'birth_date': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATE, description='Birth Date'),
        'job': openapi.Schema(type=openapi.TYPE_STRING, description='Job')
    },
    example={
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'national_code': '1234567890',
        'gender': 'male',
        'phone': 1234567890,
        'birth_date': '2000-01-01',
        'job': 'Developer'
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of personal profiles', PersonalProfileSerializer(many=True), examples={'application/json': [personal_profile_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=personal_profile_example,
    responses={
        201: openapi.Response('Personal profile created', PersonalProfileSerializer, examples={'application/json': personal_profile_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
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


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Personal profile details', PersonalProfileSerializer, examples={'application/json': personal_profile_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=personal_profile_example,
    responses={
        200: openapi.Response('Personal profile updated', PersonalProfileSerializer, examples={'application/json': personal_profile_response_example.example}),
        400: 'Bad Request - Invalid data',
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='delete',
    responses={
        204: 'No Content',
        404: 'Not Found'
    }
)
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
