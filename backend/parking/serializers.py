from rest_framework import serializers
from .models import ParkingLot, ParkingSlot

# 개별 주차 슬롯 Serializer
class ParkingSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSlot
        fields = ['slot_id', 'lot_name', 'is_occupied', 'last_updated']


# 주차장별 혼잡도 및 상태 Serializer
class ParkingLotSerializer(serializers.ModelSerializer):
    usage_rate = serializers.SerializerMethodField()  # 점유율(%) 계산용
    class Meta:
        model = ParkingLot
        fields = [
            'id', 'name', 'area',
            'total_spots', 'occupied_spots',
            'status', 'usage_rate'
        ]

    def get_usage_rate(self, obj):
        """점유율(%)을 계산해서 반환"""
        if obj.total_spots > 0:
            return round((obj.occupied_spots / obj.total_spots) * 100, 1)
        return 0