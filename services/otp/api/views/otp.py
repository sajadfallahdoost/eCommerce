from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from services.otp.logic import OTPService
from services.otp.api.serializers import (
    SendOTPEmailSerializer,
    SendOTPSMSSerializer,
    VerifyOTPEmailSerializer,
    VerifyOTPSMSSerializer
)
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
# from django.views.decorators.csrf import csrf_exempt


# Example for request body for SendOTP_email
send_otp_email_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email', example='user@example.com')
    },
    required=['email']
)

# Example for request body for SendOTP_sms
send_otp_sms_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='phone_number', example='09332368885')
    },
    required=['phone_number']
)

# Example for request body for VerifyOTP_email
verify_otp_email_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email', example='user@example.com'),
        'otp': openapi.Schema(type=openapi.TYPE_STRING, description='OTP code', example='1234')
    },
    required=['email', 'otp']
)

# Example for request body for VerifyOTP_sms
verify_otp_sms_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'phone_number': openapi.Schema(type=openapi.TYPE_STRING, description='phone_number', example='user@example.com'),
        'otp': openapi.Schema(type=openapi.TYPE_STRING, description='OTP code', example='1234')
    },
    required=['email', 'otp']
)

# Example for response body
otp_response_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'message': openapi.Schema(type=openapi.TYPE_STRING, description='Response message', example='OTP sent successfully')
    }
)


@swagger_auto_schema(
    method='post',
    request_body=send_otp_email_example,
    responses={
        200: openapi.Response('OTP sent successfully', otp_response_example),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp_email(request):
    """
    Send OTP to the user's email.
    """
    serializer = SendOTPEmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()
        otp_service = OTPService(user=user)
        otp_service.send_otp_email(email)
        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    request_body=verify_otp_email_example,
    responses={
        200: openapi.Response('OTP verified successfully', otp_response_example),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp_email(request):
    """
    Verify the OTP sent to the user's email.
    """
    serializer = VerifyOTPEmailSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        user = User.objects.filter(email=email).first()
        otp_service = OTPService(user=user)
        if otp_service.verify_otp(otp):
            return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @csrf_exempt
@swagger_auto_schema(
    method='post',
    request_body=send_otp_sms_example,
    responses={
        200: openapi.Response('OTP sent successfully', otp_response_example),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp_sms(request):
    """
    Send OTP to the user's phone number.
    """
    serializer = SendOTPSMSSerializer(data=request.data)
    if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']
        otp_service = OTPService()
        otp_service.send_otp_sms(phone_number)
        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    request_body=verify_otp_sms_example,
    responses={
        200: openapi.Response('OTP verified successfully', otp_response_example),
        400: 'Bad Request - Invalid data'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def verify_otp_sms(request):
    """
    Verify the OTP sent to the user's phone number.
    """
    serializer = VerifyOTPSMSSerializer(data=request.data)
    if serializer.is_valid():
        phone_number = serializer.validated_data['phone_number']
        otp = serializer.validated_data['otp']
        otp_service = OTPService()
        if otp_service.verify_otp(otp):
            return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
