from rest_framework import serializers


class SendOTPEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class VerifyOTPEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()


class SendOTPSMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField()


class VerifyOTPSMSSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp = serializers.CharField()
