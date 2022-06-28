from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login as login_process, logout
from django.urls import reverse, reverse_lazy

from .models import *
from .forms import CreateUserForm, UserUpdateForm
from django.views import generic

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login_process(request, user)
            return redirect("home")

    context = {}
    return render(request, 'myapp1/login.html', context)

def registration(request):
    form = CreateUserForm()
    if request.user.is_anonymous:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password1")
                form.save()
                new_user = authenticate(username=username, password=password)
                if new_user is not None:
                    login_process(request, new_user)
                    return redirect('home')
    else:
        return redirect("home")

    form = CreateUserForm()


    context = {'form': form}
    return render(request, 'myapp1/registration.html', context)

def home(request):
    return render(request, 'myapp1/home.html')
    
def profile_view(request):
    return render(request, 'myapp1/myinfo.html')

def availablejobs(request):
    return render(request, 'myapp1/availablejobs.html')

def appliedjobs(request):
    return render(request, 'myapp1/appliedjobs.html')


def developer(request):
    return render(request, 'myapp1/developer.html')



def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            return redirect('profile_view')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context= {
        'u_form': u_form
    }

    return render(request, 'myapp1/edit_profile.html', context)
