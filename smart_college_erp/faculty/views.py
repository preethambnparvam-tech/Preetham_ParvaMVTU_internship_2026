"""
Faculty App - Views
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
import csv

from .models import Faculty
from students.models import Department


@login_required
def faculty_list(request):
    faculty = Faculty.objects.select_related('department', 'user').filter(is_active=True)
    query = request.GET.get('q', '')
    dept = request.GET.get('dept', '')

    if query:
        faculty = faculty.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) |
            Q(employee_id__icontains=query) | Q(email__icontains=query)
        )
    if dept:
        faculty = faculty.filter(department__id=dept)

    paginator = Paginator(faculty, 15)
    page = paginator.get_page(request.GET.get('page'))

    return render(request, 'faculty/faculty_list.html', {
        'faculty': page,
        'departments': Department.objects.all(),
        'query': query,
        'dept': dept,
    })


@login_required
def faculty_detail(request, pk):
    member = get_object_or_404(Faculty, pk=pk)
    courses = member.teaching_courses.all()
    return render(request, 'faculty/faculty_detail.html', {'member': member, 'courses': courses})


@login_required
def faculty_create(request):
    from .forms import FacultyForm
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['employee_id'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['employee_id'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            if form.cleaned_data.get('designation') == 'hod':
                group, _ = Group.objects.get_or_create(name='HOD')
            else:
                group, _ = Group.objects.get_or_create(name='Faculty')
            user.groups.add(group)

            faculty = form.save(commit=False)
            faculty.user = user
            faculty.save()
            messages.success(request, f'Faculty {faculty.get_full_name()} added successfully.')
            return redirect('faculty:faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'faculty/faculty_form.html', {'form': form, 'title': 'Add Faculty'})


@login_required
def faculty_edit(request, pk):
    from .forms import FacultyForm
    member = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        form = FacultyForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Faculty updated.')
            return redirect('faculty:faculty_detail', pk=member.pk)
    else:
        form = FacultyForm(instance=member)
    return render(request, 'faculty/faculty_form.html', {'form': form, 'title': 'Edit Faculty'})


@login_required
def faculty_delete(request, pk):
    member = get_object_or_404(Faculty, pk=pk)
    if request.method == 'POST':
        member.is_active = False
        member.save()
        messages.success(request, 'Faculty deactivated.')
        return redirect('faculty:faculty_list')
    return render(request, 'faculty/confirm_delete.html', {'object': member})


@login_required
def export_faculty_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="faculty.csv"'
    writer = csv.writer(response)
    writer.writerow(['Employee ID', 'Name', 'Email', 'Phone', 'Designation', 'Department', 'Joining Date'])
    for f in Faculty.objects.select_related('department').all():
        writer.writerow([
            f.employee_id, f.get_full_name(), f.email, f.phone,
            f.get_designation_display(), f.department.name, f.joining_date
        ])
    return response
