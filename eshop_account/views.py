from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
def login_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        user_name = login_form.cleaned_data["user_name"]
        password = login_form.cleaned_data["password"]
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            login_form.add_error('user_name', "گذرواژه یا نام کاربری اشتباه است")
    context = {
        "login_form": login_form,
    }
    return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        user_name = register_form.cleaned_data["user_name"]
        password = register_form.cleaned_data["password"]
        email = register_form.cleaned_data["email"]
        user = User.objects.create_user(username=user_name, password=password, email=email)
        user.save()
        return redirect("/")
    context = {
        "register_form": register_form,
    }
    return render(request, 'authentication/register.html', context)
