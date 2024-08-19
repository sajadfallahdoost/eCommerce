from rest_framework import serializers


class Payment_Idpay_Serializer(serializers.Serializer):
    order_id = serializers.CharField(max_length=50)
    amount = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    phone = serializers.CharField(max_length=15, required=False, allow_blank=True)
    mail = serializers.EmailField(required=False, allow_blank=True)
    desc = serializers.CharField(max_length=255)
    callback = serializers.URLField()
