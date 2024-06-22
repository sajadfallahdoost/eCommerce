from rest_framework import serializers
from warehouse.models import Pack


class PackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pack
        fields = [
            'sku', 'price', 'buy_price', 'stock', 'actual_stock', 'is_active', 'is_default', 'product', 'att_val_ids'
        ]
