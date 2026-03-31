from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm
from .models import Student


# Create your views here.
def student_list(request):
    return render(request, "student_app/index.html")


def student_form(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_of_students')
    else:
        form = StudentRegistrationForm()
    return render(request, "student_app/form.html", {'form': form})


def student_info(request):
    return render(request, "student_app/info.html")
