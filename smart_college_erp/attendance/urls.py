"""Attendance URLs"""
from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.session_list, name='session_list'),
    path('session/create/', views.session_create, name='session_create'),
    path('session/<uuid:session_id>/mark/', views.mark_attendance, name='mark_attendance'),
    path('qr/<str:token>/', views.qr_scan_view, name='qr_scan'),
    path('report/', views.attendance_report, name='report'),
    path('export/csv/', views.export_attendance_csv, name='export_csv'),
]
