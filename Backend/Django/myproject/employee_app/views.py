from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_app/register.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_app/list.html', {'employees': employees})