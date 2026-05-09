"""
Attendance App - Models
Supports: Manual marking, QR Code attendance
"""

import uuid
from django.db import models
from students.models import Student, Course
from faculty.models import Faculty


class AttendanceSession(models.Model):
    """A session is a scheduled class where attendance is taken."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sessions')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='sessions')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    qr_code = models.ImageField(upload_to='attendance/qr/', blank=True, null=True)
    qr_token = models.CharField(max_length=64, blank=True)  # Unique token for QR
    is_active = models.BooleanField(default=True)  # Whether QR is still scannable
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course.code} | {self.date} | {self.start_time}"

    class Meta:
        ordering = ['-date', '-start_time']
        unique_together = ['course', 'date', 'start_time']


class AttendanceRecord(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    session = models.ForeignKey(
        AttendanceSession, on_delete=models.CASCADE,
        related_name='records', null=True, blank=True
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='absent')
    marked_by = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True, blank=True
    )
    marked_via_qr = models.BooleanField(default=False)
    remarks = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.roll_number} | {self.course.code} | {self.date} | {self.status}"

    class Meta:
        ordering = ['-date']
        unique_together = ['student', 'course', 'date']


class AttendanceSummary(models.Model):
    """Precomputed attendance percentages per student per course."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_classes = models.PositiveIntegerField(default=0)
    attended = models.PositiveIntegerField(default=0)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['student', 'course']

    def recalculate(self):
        records = AttendanceRecord.objects.filter(student=self.student, course=self.course)
        self.total_classes = records.count()
        self.attended = records.filter(status__in=['present', 'late']).count()
        self.percentage = (self.attended / self.total_classes * 100) if self.total_classes > 0 else 0
        self.save()
