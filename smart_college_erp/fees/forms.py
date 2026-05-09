"""Fees Forms"""
from django import forms
from .models import FeeRecord, FeeStructure


class FeeRecordForm(forms.ModelForm):
    class Meta:
        model = FeeRecord
        fields = ['student', 'fee_structure', 'description', 'amount', 'due_date', 'remarks']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'fee_structure': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '2024-2025'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
