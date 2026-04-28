from django.db import models

# Create your models here.
from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='students')
    courses = models.ManyToManyField(Course, related_name='students')

    def __str__(self):
        return self.name