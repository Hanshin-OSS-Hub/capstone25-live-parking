from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ParkingLot, ParkingSlot
from .serializers import ParkingSlotSerializer, ParkingLotSerializer
from django.conf import settings

# ✅ 전체 주차장 혼잡도 API (최신 버전)
@api_view(['GET'])
def parking_status_api(request):
    lots = ParkingLot.objects.all().order_by('area')
    serializer = ParkingLotSerializer(lots, many=True)
    return Response(serializer.data)

# ✅ 특정 슬롯 상태 변경 (시뮬레이션용)
@api_view(['POST'])
def update_parking_slot(request):
    slot_id = request.data.get('slot_id')
    is_occupied = request.data.get('is_occupied')

    try:
        slot = ParkingSlot.objects.get(slot_id=slot_id)
        slot.is_occupied = is_occupied
        slot.save()
        return Response({'message': f'{slot_id} updated successfully'})
    except ParkingSlot.DoesNotExist:
        return Response({'error': 'Slot not found'}, status=404)

# ✅ HTML 시각화 페이지 (테스트용)
def parking_status_view(request):
    lots = ParkingLot.objects.all().order_by('area')
    return render(request, 'parking_status.html', {
        'lots': lots,
        'kakao_key': settings.KAKAO_MAP_API_KEY
    })