from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student, Course, Enrollment
from .forms import StudentForm, CourseForm, EnrollmentForm
# Create your views here.

def student_list(request):
    students = Student.objects.all()
    return render(request, 'enrollment/index.html', {'students':students})

def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            messages.success(request, 'Student added successfully.')
            return redirect('list_students')
        else:
            messages.error(request, 'Failed to add student details.')
    else:
        form = StudentForm()
    return render(request, 'enrollment/student_form.html', {'form': form})

def update_student(request, id):
    student = get_object_or_404(Student, pk=id)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        messages.success(request, 'Student Details Updated Successfully.')
        return redirect('list_students')
    return render(request, 'enrollment/student_form.html', {'form': form})

def remove_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        # Hard Delete - We will use delete() method (No Backup kept)
        student.delete()
        messages.success(request, 'Student Details Deleted Successfully.')
        return redirect('list_students')
    return render(request, 'enrollment/delete_student.html', {'student':student})

def course_list(request):
    courses = Course.objects.filter(is_deleted=False)
    return render(request, 'enrollment/course_list.html', {'courses':courses})

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Course added successfully.')
            return redirect('list_courses')
        else:
            messages.error(request, 'Failed to add course details.')
    else:
        form = CourseForm()
    return render(request, 'enrollment/course_form.html', {'form': form})

def update_course(request, id):
    course = get_object_or_404(Course, pk=id)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        messages.success(request, 'Course Details Updated Successfully.')
        return redirect('list_courses')
    return render(request, 'enrollment/course_form.html', {'form': form})

def remove_course(request, id):
    course = get_object_or_404(Course, pk=id)
    if request.method == 'POST':
        # Soft Delete
        # Updating the is_deleted column to True and Data is safe as a backup in the table
        course.is_deleted = True
        course.save()
        messages.success(request, 'Course Details Deleted Successfully.')
        return redirect('list_courses')
    return render(request, 'enrollment/delete_course.html', {'course':course})

def deleted_courses(request):
    courses = Course.objects.filter(is_deleted=True)
    return render(request, 'enrollment/deleted_course.html', {'courses':courses})

def restore_course(request, id):
    course = get_object_or_404(Course, pk=id)
    course.is_deleted = False
    course.save()
    messages.success(request, 'Course Details Restored.')
    return redirect('list_courses')

def enrollment_list(request):
    enrollments = Enrollment.objects.all()
    return render(request, 'enrollment/list_enrollments.html', {'enrollments':enrollments})

def enroll_course(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            enrollment = form.save()
            messages.success(request, 'Course Enrolled successfully.')
            return redirect('list_enrollments')
        else:
            messages.error(request, 'Failed to enroll course.')
    else:
        form = EnrollmentForm()
    return render(request, 'enrollment/course_enrollment.html', {'form':form})