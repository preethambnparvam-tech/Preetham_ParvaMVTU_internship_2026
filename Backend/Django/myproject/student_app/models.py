from django.db import models

# Create your models here.
class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ] 
 
    STATE_CHOICES = [
        ('KA', 'Karnataka'),
        ('TN', 'Tamil Nadu'),
        ('AP', 'Andhra Pradesh'),
        ('TS', 'Telangana'),
        ('MH', 'Maharashtra'),
        ('KL', 'Kerala'),
    ]

    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('ISE', 'Information Science'),
        ('ECE', 'Electronics & Communication'),
        ('EEE', 'Electrical & Electronics'),
        ('ME', 'Mechanical'),
        ('CIV', 'Civil'),
        ('AIML', 'Artificial Intelligence & Machine Learning'),
        ('IOT', 'Internet of Things'),
    ]
    # charfield -> varchar(max character - 100)
    name = models.CharField(max_length=100)
    # datefield -> date (used for entering the dates)
    dob = models.DateField()
    # emailfield - > varchar, unique = true(it checks duplicate values)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10, unique=True)
    # textfield -> longtext(more brief address can be entered)
    address = models.TextField()
    # restriction has been made to select from the given options
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)
    pincode = models.IntegerField()
    branch = models.CharField(max_length=4, choices=BRANCH_CHOICES)
    # timestamps, to track the registration time & update details time
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name