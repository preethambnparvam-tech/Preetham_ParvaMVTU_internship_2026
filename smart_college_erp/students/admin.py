from django.contrib import admin
from .models import Student, Department, Course


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'hod']
    search_fields = ['name', 'code']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_number', 'get_full_name', 'department', 'semester', 'is_active']
    list_filter = ['department', 'semester', 'gender', 'is_active']
    search_fields = ['roll_number', 'first_name', 'last_name', 'email']
    list_editable = ['is_active']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'department', 'semester', 'credits', 'faculty']
    list_filter = ['department', 'semester']
    search_fields = ['name', 'code']
