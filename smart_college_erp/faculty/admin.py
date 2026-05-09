from django.contrib import admin
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'get_full_name', 'designation', 'department', 'is_active']
    list_filter = ['department', 'designation', 'is_active']
    search_fields = ['employee_id', 'first_name', 'last_name', 'email']
