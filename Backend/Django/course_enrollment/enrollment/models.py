from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    BRANCH_CHOICES = [
        ('CS', 'Computer Science'),
        ('IS', 'Information Science'),
        ('EC', 'Electronics & Communication'),
        ('EE', 'Electrical & Electronics'),
        ('AIML', 'Artificial Intelligence & Machine Learning'),
        ('IoT', 'Internet of Things'),
    ]


    name = models.CharField(max_length=50)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10,unique=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    college = models.CharField(max_length=50)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    semester = models.IntegerField()

    def __str__(self):
        return self.name
    
class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    duration = models.IntegerField()
    fees = models.IntegerField()
    # timestamp to capture the soft delete flag
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    MODE_CHOICES = [
        ('Online', 'Online Mode'),
        ('Offline', 'Offline Mode'),
        ('Hybrid', 'Hybrid Mode'),
    ]
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mode = models.CharField(max_length=10, choices=MODE_CHOICES)
    date_enrolled = models.DateField(auto_now_add=True)