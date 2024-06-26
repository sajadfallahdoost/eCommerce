from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from services.otp.logic import OTPService
from services.otp.api.serializers import SendOTPSerializer, VerifyOTPSerializer
from rest_framework.permissions import AllowAny


class SendOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SendOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp_service = OTPService()
            otp_service.send_otp(email)
            request.session['otp_secret'] = otp_service.secret
            return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VerifyOTPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            secret = request.session.get('otp_secret')
            if not secret:
                return Response({'message': 'OTP has expired or not sent'}, status=status.HTTP_400_BAD_REQUEST)
            otp_service = OTPService(secret=secret)
            if otp_service.verify_otp(otp):
                return Response({'message': 'OTP verified successfully'}, status=status.HTTP_200_OK)
            return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
