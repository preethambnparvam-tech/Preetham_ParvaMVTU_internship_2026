import random
from django.core.management.base import BaseCommand
from practice.models import Student, Branch, Course
from faker import Faker

class Command(BaseCommand):
    help = 'Seeds the database with Indian student data, branches, and courses'

    def handle(self, *args, **kwargs):
        fake = Faker('en_IN')

        # 1. Create Branches
        branches_list = ['CSE', 'ISE', 'ECE', 'EEE', 'AIML', 'IoT']
        branches = []
        for name in branches_list:
            branch, created = Branch.objects.get_or_create(name=name)
            branches.append(branch)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created branch: {name}'))

        # 2. Create Courses
        courses_list = ['Java FSWD', 'Python FSWD', 'AWS', 'AIML', 'DevOps']
        courses = []
        for name in courses_list:
            course, created = Course.objects.get_or_create(name=name)
            courses.append(course)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created course: {name}'))

        # 3. Create 50 Students
        for i in range(50):
            name = fake.name()
            email = fake.unique.email()
            phone = fake.phone_number()
            branch = random.choice(branches)
            
            student = Student.objects.create(
                name=name,
                email=email,
                phone=phone,
                branch=branch
            )
            
            # Randomly assign 1-3 courses to each student
            assigned_courses = random.sample(courses, k=random.randint(1, 3))
            student.courses.add(*assigned_courses)
            
            self.stdout.write(f'Created student {i+1}: {name}')

        self.stdout.write(self.style.SUCCESS('Successfully seeded 50 students!'))