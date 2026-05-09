"""
Faculty App - Models
"""

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Faculty(models.Model):
    DESIGNATION_CHOICES = [
        ('professor', 'Professor'),
        ('associate_professor', 'Associate Professor'),
        ('assistant_professor', 'Assistant Professor'),
        ('lecturer', 'Lecturer'),
        ('hod', 'Head of Department'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_profile')
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit number')]
    )
    designation = models.CharField(max_length=30, choices=DESIGNATION_CHOICES)
    department = models.ForeignKey(
        'students.Department', on_delete=models.PROTECT, related_name='faculty_members'
    )
    qualification = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    joining_date = models.DateField()
    profile_photo = models.ImageField(upload_to='faculty/photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.employee_id} - {self.get_full_name()}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['department', 'last_name']
        verbose_name_plural = 'Faculty'
