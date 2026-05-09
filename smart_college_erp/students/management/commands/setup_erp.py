"""
Custom management command to set up initial data:
  - Creates user groups (Admin, HOD, Faculty, Student)
  - Creates a default superuser
  - Creates sample departments

Usage:
  python manage.py setup_erp
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission


class Command(BaseCommand):
    help = 'Sets up initial groups, permissions, and a default admin user for the ERP.'

    def add_arguments(self, parser):
        parser.add_argument('--username', default='admin', help='Admin username')
        parser.add_argument('--password', default='admin123', help='Admin password')
        parser.add_argument('--email', default='admin@college.edu', help='Admin email')

    def handle(self, *args, **options):
        self.stdout.write(self.style.MIGRATE_HEADING('Setting up Smart College ERP...'))

        # ── Create Groups ──────────────────────────────────────
        groups = ['Admin', 'HOD', 'Faculty', 'Student']
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)
            if created:
                self.stdout.write(f'  ✓ Created group: {group_name}')
            else:
                self.stdout.write(f'  · Group already exists: {group_name}')

        # ── Create Superuser ───────────────────────────────────
        username = options['username']
        password = options['password']
        email = options['email']

        if not User.objects.filter(username=username).exists():
            user = User.objects.create_superuser(
                username=username,
                password=password,
                email=email,
                first_name='System',
                last_name='Admin'
            )
            admin_group = Group.objects.get(name='Admin')
            user.groups.add(admin_group)
            self.stdout.write(
                self.style.SUCCESS(f'  ✓ Created superuser: {username} / {password}')
            )
        else:
            self.stdout.write(f'  · Superuser "{username}" already exists.')

        # ── Create Sample Departments ──────────────────────────
        try:
            from students.models import Department
            sample_depts = [
                {'name': 'Computer Science Engineering', 'code': 'CSE'},
                {'name': 'Electronics & Communication', 'code': 'ECE'},
                {'name': 'Mechanical Engineering', 'code': 'ME'},
                {'name': 'Civil Engineering', 'code': 'CE'},
                {'name': 'Information Science', 'code': 'ISE'},
            ]
            for d in sample_depts:
                dept, created = Department.objects.get_or_create(code=d['code'], defaults={'name': d['name']})
                if created:
                    self.stdout.write(f'  ✓ Created department: {d["code"]} - {d["name"]}')
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'  ⚠ Could not create departments: {e}'))

        self.stdout.write(self.style.SUCCESS('\n✅ Setup complete! Visit http://127.0.0.1:8000/login/ to start.'))
        self.stdout.write(f'   Login: {options["username"]} / {options["password"]}')
