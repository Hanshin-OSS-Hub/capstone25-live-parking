from django.db import models

class ParkingLot(models.Model):
    name = models.CharField(max_length=50)              # 주차장 이름 (ex: 정문 주차장)
    area = models.CharField(max_length=10)              # 구역명 (A, B, C 등)
    total_spots = models.IntegerField()                 # 전체 주차면 수
    occupied_spots = models.IntegerField(default=0)     # 현재 주차된 차량 수
    status = models.CharField(max_length=20, default='여유')  # 혼잡도 상태 (자동 계산됨)

    def save(self, *args, **kwargs):
        """혼잡도 상태 자동 업데이트"""
        usage_rate = self.occupied_spots / self.total_spots if self.total_spots > 0 else 0
        if usage_rate >= 0.8:
            self.status = "혼잡"
        elif usage_rate >= 0.4:
            self.status = "보통"
        else:
            self.status = "여유"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.area})"


class ParkingSlot(models.Model):
    slot_id = models.CharField(max_length=10, unique=True)  # 예: A1, A2
    lot_name = models.CharField(max_length=50, default="Default Lot")  # 속한 주차장명
    is_occupied = models.BooleanField(default=False)         # 주차 여부
    last_updated = models.DateTimeField(auto_now=True)       # 마지막 변경 시각

    def __str__(self):
        return f"{self.lot_name} - {self.slot_id} ({'사용중' if self.is_occupied else '비어있음'})"