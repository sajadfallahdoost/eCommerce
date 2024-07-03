from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from account.models import CorporateProfile
from account.api.serializers import CorporateProfileSerializer
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body
corporate_profile_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name'),
        'national_code': openapi.Schema(type=openapi.TYPE_INTEGER, description='National Code'),
        'register_number': openapi.Schema(type=openapi.TYPE_INTEGER, description='Register Number'),
        'economical_code': openapi.Schema(type=openapi.TYPE_INTEGER, description='Economical Code', nullable=True),
        'phone': openapi.Schema(type=openapi.TYPE_INTEGER, description='Phone')
    },
    required=['name', 'national_code', 'register_number', 'phone'],
    example={
        'name': 'Company Inc.',
        'national_code': 123456789,
        'register_number': 987654321,
        'economical_code': 1122334455,
        'phone': 1234567890
    }
)

# Example for response body
corporate_profile_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the corporate profile'),
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='Name'),
        'national_code': openapi.Schema(type=openapi.TYPE_INTEGER, description='National Code'),
        'register_number': openapi.Schema(type=openapi.TYPE_INTEGER, description='Register Number'),
        'economical_code': openapi.Schema(type=openapi.TYPE_INTEGER, description='Economical Code', nullable=True),
        'phone': openapi.Schema(type=openapi.TYPE_INTEGER, description='Phone')
    },
    example={
        'id': 1,
        'name': 'Company Inc.',
        'national_code': 123456789,
        'register_number': 987654321,
        'economical_code': 1122334455,
        'phone': 1234567890
    }
)


@swagger_auto_schema(
    method='get',
    responses={200: openapi.Response('List of corporate profiles', CorporateProfileSerializer(many=True), examples={'application/json': [corporate_profile_response_example.example]})}
)
@swagger_auto_schema(
    method='post',
    request_body=corporate_profile_example,
    responses={
        201: openapi.Response('Corporate profile created', CorporateProfileSerializer, examples={'application/json': corporate_profile_response_example.example}),
        400: 'Bad Request - Invalid data'
    }
)
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


@swagger_auto_schema(
    method='get',
    responses={
        200: openapi.Response('Corporate profile details', CorporateProfileSerializer, examples={'application/json': corporate_profile_response_example.example}),
        404: 'Not Found'
    }
)
@swagger_auto_schema(
    method='put',
    request_body=corporate_profile_example,
    responses={
        200: openapi.Response('Corporate profile updated', CorporateProfileSerializer, examples={'application/json': corporate_profile_response_example.example}),
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
