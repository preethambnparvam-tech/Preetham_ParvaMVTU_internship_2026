"""
Smart College ERP - Core Views
"""

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from students.models import Student, Department, Course
from faculty.models import Faculty
from attendance.models import AttendanceRecord
from fees.models import FeeRecord
from django.utils import timezone
from django.db.models import Count, Q


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('login')


@login_required
def dashboard(request):
    user = request.user
    role = get_user_role(user)
    context = {'role': role, 'user': user}

    if role == 'admin' or user.is_superuser:
        context.update({
            'total_students': Student.objects.filter(is_active=True).count(),
            'total_faculty': Faculty.objects.filter(is_active=True).count(),
            'total_departments': Department.objects.count(),
            'total_courses': Course.objects.count(),
            'pending_fees': FeeRecord.objects.filter(status='pending').count(),
            'today_attendance': AttendanceRecord.objects.filter(date=timezone.now().date()).count(),
            'recent_students': Student.objects.order_by('-created_at')[:5],
        })
    elif role == 'faculty':
        try:
            faculty = Faculty.objects.get(user=user)
            context.update({
                'faculty': faculty,
                'today_classes': faculty.timetable_set.filter(
                    day_of_week=timezone.now().strftime('%A')
                ).count() if hasattr(faculty, 'timetable_set') else 0,
            })
        except Faculty.DoesNotExist:
            pass
    elif role == 'student':
        try:
            student = Student.objects.get(user=user)
            context.update({
                'student': student,
                'fee_status': FeeRecord.objects.filter(student=student, status='pending').count(),
            })
        except Student.DoesNotExist:
            pass

    return render(request, 'base/dashboard.html', context)


def get_user_role(user):
    """Helper to determine user role from groups."""
    if user.is_superuser:
        return 'admin'
    groups = user.groups.values_list('name', flat=True)
    if 'Admin' in groups:
        return 'admin'
    elif 'HOD' in groups:
        return 'hod'
    elif 'Faculty' in groups:
        return 'faculty'
    elif 'Student' in groups:
        return 'student'
    return 'admin'  # default for staff
