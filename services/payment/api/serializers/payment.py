from rest_framework import serializers


class MetadataSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15, required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)


class PaymentRequestSerializer(serializers.Serializer):
    merchant_id = serializers.CharField(max_length=36)
    amount = serializers.IntegerField()
    description = serializers.CharField(max_length=255)
    callback_url = serializers.URLField()
    metadata = MetadataSerializer()
