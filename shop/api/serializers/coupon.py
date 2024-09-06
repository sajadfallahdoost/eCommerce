'''
from rest_framework import serializers
from .models import CouponModel  # Assuming your model is in the same app

class CouponModelSerializer(serializers.ModelSerializer):
    used_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)  # Show only user IDs

    class Meta:
        model = CouponModel
        fields = '__all__'  # Include all fields

 Optional: If you want to exclude specific fields
 class CouponModelSerializer(serializers.ModelSerializer):
     used_by = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

     class Meta:
         model = CouponModel
         exclude = ['created_date', 'updated_date']  # Exclude these fields
'''