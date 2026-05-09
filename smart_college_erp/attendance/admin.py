from django.contrib import admin
from .models import AttendanceSession, AttendanceRecord, AttendanceSummary


@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = ['course', 'faculty', 'date', 'start_time', 'is_active']
    list_filter = ['course__department', 'date', 'is_active']


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'date', 'status', 'marked_via_qr']
    list_filter = ['status', 'course', 'date', 'marked_via_qr']
    search_fields = ['student__roll_number', 'student__first_name']


@admin.register(AttendanceSummary)
class AttendanceSummaryAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'total_classes', 'attended', 'percentage']
    list_filter = ['course__department']
