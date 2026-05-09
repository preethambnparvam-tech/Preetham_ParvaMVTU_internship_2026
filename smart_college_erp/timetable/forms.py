"""Timetable Forms"""
from django import forms
from .models import Timetable, TimeSlot


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'
        widgets = {
            'department': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'day_of_week': forms.Select(attrs={'class': 'form-select'}),
            'time_slot': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'faculty': forms.Select(attrs={'class': 'form-select'}),
            'room': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. A-101'}),
        }


class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['start_time', 'end_time', 'label']
        widgets = {
            'start_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'label': forms.TextInput(attrs={'class': 'form-control'}),
        }
