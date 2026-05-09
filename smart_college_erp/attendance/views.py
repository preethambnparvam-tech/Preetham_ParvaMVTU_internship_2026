"""
Attendance App - Views
Handles: Session creation, manual marking, QR generation & scanning
"""

import uuid
import secrets
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.db.models import Q

from .models import AttendanceSession, AttendanceRecord, AttendanceSummary
from students.models import Student, Course
from faculty.models import Faculty
from .forms import AttendanceSessionForm, BulkAttendanceForm


@login_required
def session_list(request):
    sessions = AttendanceSession.objects.select_related('course', 'faculty').all()
    return render(request, 'attendance/session_list.html', {'sessions': sessions})


@login_required
def session_create(request):
    if request.method == 'POST':
        form = AttendanceSessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.qr_token = secrets.token_urlsafe(32)
            # Generate QR code
            try:
                import qrcode
                from io import BytesIO
                from django.core.files import File

                qr_data = f"{request.build_absolute_uri('/attendance/qr/')}{session.qr_token}/"
                qr_img = qrcode.make(qr_data)
                buffer = BytesIO()
                qr_img.save(buffer, format='PNG')
                session.qr_code.save(f'qr_{session.qr_token}.png', File(buffer), save=False)
            except ImportError:
                pass  # qrcode not installed, skip QR generation

            session.save()
            messages.success(request, 'Session created. QR code generated.')
            return redirect('attendance:mark_attendance', session_id=session.pk)
    else:
        form = AttendanceSessionForm()
    return render(request, 'attendance/session_form.html', {'form': form})


@login_required
def mark_attendance(request, session_id):
    session = get_object_or_404(AttendanceSession, pk=session_id)
    students = Student.objects.filter(
        department=session.course.department,
        semester=session.course.semester,
        is_active=True
    ).order_by('roll_number')

    # Pre-populate existing records
    existing = {
        r.student_id: r for r in
        AttendanceRecord.objects.filter(session=session)
    }

    if request.method == 'POST':
        for student in students:
            status = request.POST.get(f'status_{student.pk}', 'absent')
            record, created = AttendanceRecord.objects.get_or_create(
                student=student,
                course=session.course,
                date=session.date,
                defaults={
                    'session': session,
                    'status': status,
                    'marked_by': getattr(request.user, 'faculty_profile', None)
                }
            )
            if not created:
                record.status = status
                record.save()

        # Update summaries
        for student in students:
            summary, _ = AttendanceSummary.objects.get_or_create(
                student=student, course=session.course
            )
            summary.recalculate()

        messages.success(request, f'Attendance marked for {students.count()} students.')
        return redirect('attendance:session_list')

    return render(request, 'attendance/mark_attendance.html', {
        'session': session,
        'students': students,
        'existing': existing,
        'status_choices': AttendanceRecord.STATUS_CHOICES,
    })


@login_required
def qr_scan_view(request, token):
    """Handles QR code scanning by students."""
    try:
        session = AttendanceSession.objects.get(qr_token=token, is_active=True)
    except AttendanceSession.DoesNotExist:
        return render(request, 'attendance/qr_expired.html')

    now = timezone.localtime()
    
    if session.date != now.date():
        messages.error(request, 'This attendance session is not scheduled for today.')
        return redirect('dashboard')
        
    current_time = now.time()
    if current_time < session.start_time:
        messages.error(request, 'This class has not started yet. You cannot mark attendance before the class starts.')
        return redirect('dashboard')
        
    if current_time > session.end_time:
        messages.error(request, 'The time to mark attendance for this class is over.')
        return redirect('dashboard')

    try:
        student = request.user.student_profile
    except Student.DoesNotExist:
        messages.error(request, 'Only students can mark attendance via QR.')
        return redirect('dashboard')

    record, created = AttendanceRecord.objects.get_or_create(
        student=student,
        course=session.course,
        date=session.date,
        defaults={
            'session': session,
            'status': 'present',
            'marked_via_qr': True,
        }
    )

    if created:
        summary, _ = AttendanceSummary.objects.get_or_create(student=student, course=session.course)
        summary.recalculate()
        messages.success(request, f'✓ Attendance marked for {session.course.name}')
    else:
        messages.info(request, 'Attendance already marked for this session.')

    return render(request, 'attendance/qr_success.html', {'session': session, 'created': created})


@login_required
def attendance_report(request):
    """View student-wise attendance summary."""
    dept = request.GET.get('dept', '')
    course_id = request.GET.get('course', '')

    summaries = AttendanceSummary.objects.select_related('student', 'course')
    if dept:
        summaries = summaries.filter(student__department__id=dept)
    if course_id:
        summaries = summaries.filter(course__id=course_id)

    # Flag students below 75%
    low_attendance = summaries.filter(percentage__lt=75)

    return render(request, 'attendance/report.html', {
        'summaries': summaries,
        'low_attendance': low_attendance,
        'courses': Course.objects.all(),
    })


@login_required
def export_attendance_csv(request):
    import csv
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="attendance_report.csv"'
    writer = csv.writer(response)
    writer.writerow(['Roll No', 'Student Name', 'Course', 'Total Classes', 'Attended', 'Percentage'])

    for s in AttendanceSummary.objects.select_related('student', 'course').all():
        writer.writerow([
            s.student.roll_number, s.student.get_full_name(),
            s.course.code, s.total_classes, s.attended, f"{s.percentage}%"
        ])
    return response
