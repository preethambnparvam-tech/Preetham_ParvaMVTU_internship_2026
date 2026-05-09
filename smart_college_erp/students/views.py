"""
Students App - Views
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator
from django.template.loader import render_to_string
import csv
import io

from .models import Student, Department, Course
from .forms import StudentForm, DepartmentForm, CourseForm


# ──────────────────────────────────────────────────────────────
# DEPARTMENT VIEWS
# ──────────────────────────────────────────────────────────────

@login_required
def department_list(request):
    departments = Department.objects.all().prefetch_related('students', 'courses')
    return render(request, 'students/department_list.html', {'departments': departments})


@login_required
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department created successfully.')
            return redirect('students:department_list')
    else:
        form = DepartmentForm()
    return render(request, 'students/department_form.html', {'form': form, 'title': 'Add Department'})


@login_required
def department_edit(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=dept)
        if form.is_valid():
            form.save()
            messages.success(request, 'Department updated successfully.')
            return redirect('students:department_list')
    else:
        form = DepartmentForm(instance=dept)
    return render(request, 'students/department_form.html', {'form': form, 'title': 'Edit Department'})


@login_required
def department_delete(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    if request.method == 'POST':
        dept.delete()
        messages.success(request, 'Department deleted.')
        return redirect('students:department_list')
    return render(request, 'students/confirm_delete.html', {'object': dept, 'type': 'Department'})


# ──────────────────────────────────────────────────────────────
# STUDENT VIEWS
# ──────────────────────────────────────────────────────────────

@login_required
def student_list(request):
    students = Student.objects.select_related('department', 'user').filter(is_active=True)
    query = request.GET.get('q', '')
    dept_filter = request.GET.get('dept', '')
    sem_filter = request.GET.get('sem', '')

    if query:
        students = students.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(roll_number__icontains=query) |
            Q(email__icontains=query)
        )
    if dept_filter:
        students = students.filter(department__id=dept_filter)
    if sem_filter:
        students = students.filter(semester=sem_filter)

    paginator = Paginator(students, 20)
    page = request.GET.get('page')
    students_page = paginator.get_page(page)

    departments = Department.objects.all()
    semesters = range(1, 9)

    return render(request, 'students/student_list.html', {
        'students': students_page,
        'departments': departments,
        'semesters': semesters,
        'query': query,
        'dept_filter': dept_filter,
        'sem_filter': sem_filter,
    })


@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    from attendance.models import AttendanceRecord
    from fees.models import FeeRecord
    attendance = AttendanceRecord.objects.filter(student=student).order_by('-date')[:10]
    fees = FeeRecord.objects.filter(student=student).order_by('-due_date')
    return render(request, 'students/student_detail.html', {
        'student': student,
        'attendance': attendance,
        'fees': fees,
    })


@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            # Create auth user
            user = User.objects.create_user(
                username=form.cleaned_data['roll_number'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['roll_number'],  # Default password = roll_number
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            student_group, _ = Group.objects.get_or_create(name='Student')
            user.groups.add(student_group)

            student = form.save(commit=False)
            student.user = user
            student.save()

            messages.success(request, f'Student {student.get_full_name()} added. Default password is roll number.')
            return redirect('students:student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Add Student'})


@login_required
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            student = form.save()
            # Sync user info
            student.user.first_name = student.first_name
            student.user.last_name = student.last_name
            student.user.email = student.email
            student.user.save()
            messages.success(request, 'Student updated successfully.')
            return redirect('students:student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form, 'title': 'Edit Student', 'student': student})


@login_required
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.is_active = False  # Soft delete
        student.save()
        messages.success(request, 'Student deactivated.')
        return redirect('students:student_list')
    return render(request, 'students/confirm_delete.html', {'object': 'student', 'type': 'Student'})


# ──────────────────────────────────────────────────────────────
# EXPORT VIEWS
# ──────────────────────────────────────────────────────────────

@login_required
def export_students_csv(request):
    """Export all students to CSV (Excel-compatible)."""
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="students.csv"'

    writer = csv.writer(response)
    writer.writerow([
        'Roll Number', 'First Name', 'Last Name', 'Email', 'Phone',
        'Gender', 'Date of Birth', 'Blood Group', 'Department',
        'Semester', 'Admission Year', 'Parent Name', 'Parent Phone', 'Active'
    ])

    students = Student.objects.select_related('department').all()
    for s in students:
        writer.writerow([
            s.roll_number, s.first_name, s.last_name, s.email, s.phone,
            s.get_gender_display(), s.date_of_birth, s.blood_group,
            s.department.name, s.semester, s.admission_year,
            s.parent_name, s.parent_phone, s.is_active
        ])

    return response


@login_required
def export_students_pdf(request):
    """Export students list to PDF using WeasyPrint or xhtml2pdf."""
    try:
        from weasyprint import HTML
        students = Student.objects.select_related('department').filter(is_active=True)
        html_string = render_to_string('students/pdf_student_list.html', {'students': students})
        html = HTML(string=html_string)
        pdf = html.write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="students_report.pdf"'
        return response
    except ImportError:
        messages.error(request, 'PDF export requires WeasyPrint. Install with: pip install weasyprint')
        return redirect('students:student_list')


# ──────────────────────────────────────────────────────────────
# COURSE VIEWS
# ──────────────────────────────────────────────────────────────

@login_required
def course_list(request):
    courses = Course.objects.select_related('department', 'faculty').all()
    return render(request, 'students/course_list.html', {'courses': courses})


@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course created.')
            return redirect('students:course_list')
    else:
        form = CourseForm()
    return render(request, 'students/course_form.html', {'form': form, 'title': 'Add Course'})


@login_required
def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated.')
            return redirect('students:course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'students/course_form.html', {'form': form, 'title': 'Edit Course'})
