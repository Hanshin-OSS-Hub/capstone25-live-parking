from django.urls import path
from . import views

urlpatterns = [
    path('', views.parking_status_view, name='parking_status_view'),
    path('status/', views.parking_status_api, name='parking_status_api'),
    path('update/', views.update_parking_slot, name='update_parking_slot'),
    #path('summary/', views.parking_lot_summary, name='parking_lot_summary'),
]