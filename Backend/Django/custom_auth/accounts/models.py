from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    SEMESTER_CHOICES = [(str(i), f'Semester {i}') for i in range(1, 9)]

    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    usn = models.CharField(max_length=10, blank=True, null=True, verbose_name="USN")
    college = models.CharField(max_length=100, blank=True, null=True)
    branch = models.CharField(max_length=50, blank=True, null=True)
    semester = models.CharField(max_length=2, choices=SEMESTER_CHOICES, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    temporary_address = models.TextField(blank=True, null=True)
    permanent_address = models.TextField(blank=True, null=True)
    terms_agreed = models.BooleanField(default=False)

    def __str__(self):
        return self.username

