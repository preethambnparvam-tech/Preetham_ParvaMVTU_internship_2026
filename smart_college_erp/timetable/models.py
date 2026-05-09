"""
Timetable App - Models
"""

import uuid
from django.db import models
from students.models import Department, Course
from faculty.models import Faculty


class TimeSlot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    label = models.CharField(max_length=30, blank=True)  # e.g. "9:00 - 10:00"

    def __str__(self):
        return self.label or f"{self.start_time} - {self.end_time}"

    def save(self, *args, **kwargs):
        if not self.label:
            self.label = f"{self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['start_time']


class Timetable(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='timetables')
    semester = models.IntegerField(choices=Course.SEMESTER_CHOICES)
    day_of_week = models.CharField(max_length=10, choices=DAY_CHOICES)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True)
    room = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.department.code} | Sem {self.semester} | {self.day_of_week} | {self.time_slot}"

    class Meta:
        ordering = ['day_of_week', 'time_slot']
        unique_together = ['department', 'semester', 'day_of_week', 'time_slot']
