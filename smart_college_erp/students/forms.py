"""
Students App - Forms
"""

from django import forms
from .models import Student, Department, Course


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'code', 'hod']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Computer Science'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. CSE'}),
            'hod': forms.Select(attrs={'class': 'form-select'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'created_at', 'updated_at', 'is_active']
        widgets = {
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'admission_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'parent_name': forms.TextInput(attrs={'class': 'form-control'}),
            'parent_phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control'}),
            'faculty': forms.Select(attrs={'class': 'form-select'}),
        }
