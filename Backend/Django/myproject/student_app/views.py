from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentRegistrationForm
from .models import Student


# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, "student_app/index.html", {'students': students})



def student_form(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_students')
    else:
        form = StudentRegistrationForm()
    return render(request, "student_app/form.html", {'form': form})


def student_info(request, pk):
    student = get_object_or_404(Student, id=pk)
    return render(request, "student_app/info.html", {'student': student})

def edit_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_of_students')
    else:
        form = StudentRegistrationForm(instance=student)
    return render(request, "student_app/form.html", {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, id=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('list_of_students')
    return render(request, "student_app/delete.html", {'student': student})
