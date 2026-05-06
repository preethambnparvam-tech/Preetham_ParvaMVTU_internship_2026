from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "User Registered Successfully!")
            return redirect('signin')
    else:
            form = RegistrationForm()
    return render(request, 'authentication/signup.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get('username')
            pwd = form.cleaned_data.get('password')
            user = authenticate(username=uname, password=pwd)
            if user:
                login(request, user)
                return redirect('welcome')
            else:
                messages.error(request, "Invalid Credentials, Please try again!")
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/signin.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def user_dashboard(request):
    return render(request, 'authentication/dashboard.html')