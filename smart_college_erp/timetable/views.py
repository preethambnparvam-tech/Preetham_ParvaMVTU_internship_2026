"""Timetable Views"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Timetable, TimeSlot
from students.models import Department
from .forms import TimetableForm, TimeSlotForm


@login_required
def timetable_view(request):
    dept = request.GET.get('dept', '')
    sem = request.GET.get('sem', '')

    timetables = Timetable.objects.select_related('course', 'faculty', 'time_slot')
    if dept:
        timetables = timetables.filter(department__id=dept)
    if sem:
        timetables = timetables.filter(semester=sem)

    # Organize by day
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    time_slots = TimeSlot.objects.all()
    schedule = {day: {} for day in days}

    for entry in timetables:
        schedule[entry.day_of_week][entry.time_slot_id] = entry

    return render(request, 'timetable/view.html', {
        'schedule': schedule,
        'days': days,
        'time_slots': time_slots,
        'departments': Department.objects.all(),
        'semesters': range(1, 9),
        'dept': dept, 'sem': sem,
    })


@login_required
def timetable_create(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Timetable entry added.')
            return redirect('timetable:view')
    else:
        form = TimetableForm()
    return render(request, 'timetable/form.html', {'form': form})


@login_required
def timetable_delete(request, pk):
    entry = get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Entry removed.')
        return redirect('timetable:view')
    return render(request, 'timetable/confirm_delete.html', {'entry': entry})


@login_required
def timeslot_create(request):
    if request.method == 'POST':
        form = TimeSlotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Time slot created.')
            return redirect('timetable:view')
    else:
        form = TimeSlotForm()
    return render(request, 'timetable/timeslot_form.html', {'form': form})
