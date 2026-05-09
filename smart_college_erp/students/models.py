"""
Students App - Models
Handles: Department, Course, Student management
"""

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)
    hod = models.ForeignKey(
        'faculty.Faculty', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='headed_department'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ['name']


class Course(models.Model):
    SEMESTER_CHOICES = [(i, f'Semester {i}') for i in range(1, 9)]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=15, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    credits = models.PositiveSmallIntegerField(default=3)
    faculty = models.ForeignKey(
        'faculty.Faculty', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='teaching_courses'
    )

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        ordering = ['department', 'semester', 'name']


class Student(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('O', 'Other')]
    BLOOD_GROUPS = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    BLOOD_CHOICES = [(b, b) for b in BLOOD_GROUPS]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number')]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=3, choices=BLOOD_CHOICES, blank=True)
    address = models.TextField(blank=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name='students')
    semester = models.IntegerField(choices=Course.SEMESTER_CHOICES, default=1)
    admission_year = models.PositiveSmallIntegerField()
    profile_photo = models.ImageField(upload_to='students/photos/', blank=True, null=True)
    parent_name = models.CharField(max_length=100, blank=True)
    parent_phone = models.CharField(max_length=10, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.roll_number} - {self.get_full_name()}"

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['roll_number']
