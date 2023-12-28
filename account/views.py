from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from account.forms import UserRegistrationForm, UserLoginForm
from account.models import EmployerProfile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data['password'])
            user.save()
            user_type = form.cleaned_data['user_type']
            if user_type == 'E':
                EmployerProfile.objects.create(user=user)
            login(request, user)
            return redirect('service:feed')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html',
                  {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['email'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('service:feed')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html',
                  {'form': form})


def user_logout(request):
    logout(request)
    return redirect('service:feed')
