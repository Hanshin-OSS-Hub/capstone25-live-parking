from django.contrib import admin
from .models import ParkingLot, ParkingSlot

@admin.register(ParkingLot)
class ParkingLotAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'total_spots', 'occupied_spots', 'status_display')
    list_editable = ('occupied_spots',)
    search_fields = ('name', 'area')
    list_filter = ('status',)

    def status_display(self, obj):
        """관리자 페이지에서 혼잡도 상태 컬럼 표시"""
        return obj.status
    status_display.short_description = "혼잡도 상태"

@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_id', 'lot_name', 'is_occupied', 'last_updated')
    list_editable = ('is_occupied',)
    search_fields = ('slot_id', 'lot_name')