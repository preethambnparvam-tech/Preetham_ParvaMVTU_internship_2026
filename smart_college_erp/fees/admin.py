from django.contrib import admin
from .models import FeeRecord, FeeStructure


@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'semester', 'amount', 'academic_year', 'is_active']
    list_filter = ['department', 'semester', 'academic_year']


@admin.register(FeeRecord)
class FeeRecordAdmin(admin.ModelAdmin):
    list_display = ['receipt_number', 'student', 'description', 'amount', 'amount_paid', 'status', 'due_date']
    list_filter = ['status', 'payment_method']
    search_fields = ['student__roll_number', 'student__first_name', 'receipt_number']
