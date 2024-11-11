from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from docs.models import Record, CityLocation
from .forms import RegisterForm, LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:index')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'authentication/login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully. Please check your email to activate your account.')
            return redirect('authentication:login')
        else:
            messages.error(
                request, 'Account creation failed. Please try again.')
    else:
        form = RegisterForm()
    city_locations = CityLocation.objects.all()
    context = {
        'form': form,
        'city_locations': city_locations,
    }
    return render(request, 'authentication/register.html', context=context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('authentication:login')


@login_required
def user_profile(request):
    appointments = Record.objects.filter(user=request.user)
    context = {
        "appointments": appointments
    }
    return render(request, 'authentication/profile.html', context=context)
