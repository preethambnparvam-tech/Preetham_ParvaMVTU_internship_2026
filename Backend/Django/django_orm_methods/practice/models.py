from django.db import models

class Branch(models.Model):
    short_name = models.CharField(max_length=10)
    long_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.short_name} - {self.long_name}"

class Course(models.Model):
    short_name = models.CharField(max_length=20)
    long_name = models.CharField(max_length=100)
    duration = models.IntegerField(help_text="Duration in months")
    fees = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.short_name} ({self.duration} Months)"

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    SEM_CHOICES = [
        (2, '2nd Semester'),
        (4, '4th Semester'),
        (6, '6th Semester'),
        (8, '8th Semester'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    sem = models.IntegerField(choices=SEM_CHOICES)
    registration_date = models.DateField(null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='students')
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name