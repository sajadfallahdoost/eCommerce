from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from services.otp.logic import OTPService
from services.otp.api.serializers import SendOTPSerializer, VerifyOTPSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Example for request body for SendOTP
send_otp_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email', example='user@example.com')
    },
    required=['email']
)

# Example for request body for VerifyOTP
verify_otp_example = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email', example='user@example.com'),
        'otp': openapi.Schema(type=openapi.TYPE_STRING, description='OTP code', example='123456')
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
    request_body=send_otp_example,
    responses={
        200: openapi.Response('OTP sent successfully', otp_response_example),
        400: 'Bad Request - Invalid data',
        404: 'Not Found'
    }
)
@api_view(['POST'])
@permission_classes([AllowAny])
def send_otp(request):
    """
    Send OTP to the user's email.
    """
    serializer = SendOTPSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        try:
            user = User.objects.get(email=email)
            otp_service = OTPService(user)
            otp_service.send_otp(email)
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='post',
    request_body=verify_otp_example,
    responses={
        200: openapi.Response('OTP verified successfully', otp_response_example),
        400: 'Bad Request - Invalid data',
        404: 'Not Found'
    }
)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_otp(request):
    """
    Verify the OTP sent to the user's email.
    """
    serializer = VerifyOTPSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        otp = serializer.validated_data['otp']
        try:
            user = User.objects.get(email=email)
            otp_service = OTPService(user)
            if otp_service.verify_otp(otp):
                return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
# from services.otp.logic import OTPService
# from services.otp.api.serializers import SendOTPSerializer, VerifyOTPSerializer
# from rest_framework.permissions import AllowAny, IsAuthenticated


# class SendOTPView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = SendOTPSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             try:
#                 user = User.objects.get(email=email)
#                 otp_service = OTPService(user)
#                 otp_service.send_otp(email)
#                 return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class VerifyOTPView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = VerifyOTPSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['email']
#             otp = serializer.validated_data['otp']
#             try:
#                 user = User.objects.get(email=email)
#                 otp_service = OTPService(user)
#                 if otp_service.verify_otp(otp):
#                     return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
#                 else:
#                     return Response({'message': 'Invalid or expired OTP'}, status=status.HTTP_400_BAD_REQUEST)
#             except User.DoesNotExist:
#                 return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
