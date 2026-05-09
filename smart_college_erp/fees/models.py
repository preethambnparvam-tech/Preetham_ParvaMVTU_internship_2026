"""
Fees App - Models
"""

import uuid
from django.db import models
from students.models import Student


class FeeStructure(models.Model):
    SEMESTER_CHOICES = [(i, f'Semester {i}') for i in range(1, 9)]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)  # e.g. "Tuition Fee", "Lab Fee"
    department = models.ForeignKey(
        'students.Department', on_delete=models.CASCADE, related_name='fee_structures'
    )
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    academic_year = models.CharField(max_length=9)  # e.g. "2024-2025"
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} | {self.department.code} | Sem {self.semester} | ₹{self.amount}"

    class Meta:
        ordering = ['department', 'semester']


class FeeRecord(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('partial', 'Partial'),
        ('overdue', 'Overdue'),
        ('waived', 'Waived'),
    ]
    PAYMENT_METHODS = [
        ('cash', 'Cash'),
        ('upi', 'UPI'),
        ('neft', 'NEFT/RTGS'),
        ('dd', 'Demand Draft'),
        ('card', 'Card'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fee_records')
    fee_structure = models.ForeignKey(
        FeeStructure, on_delete=models.PROTECT, null=True, blank=True
    )
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    due_date = models.DateField()
    paid_date = models.DateField(null=True, blank=True)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHODS, blank=True)
    transaction_id = models.CharField(max_length=100, blank=True)
    receipt_number = models.CharField(max_length=50, unique=True, blank=True)
    remarks = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.roll_number} | {self.description} | {self.status}"

    @property
    def balance(self):
        return self.amount - self.amount_paid

    def save(self, *args, **kwargs):
        # Auto-generate receipt number
        if not self.receipt_number and self.status == 'paid':
            import datetime
            self.receipt_number = f"RCP{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-due_date']
