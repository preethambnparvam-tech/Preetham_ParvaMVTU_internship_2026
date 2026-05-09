from django.contrib import admin
from .models import TimeSlot, Timetable


@admin.register(TimeSlot)
class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ['label', 'start_time', 'end_time']


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ['department', 'semester', 'day_of_week', 'time_slot', 'course', 'faculty', 'room']
    list_filter = ['department', 'semester', 'day_of_week']
