from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, get_user_model, logout


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
    context = {
        "login_form": login_form,
    }
    return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('/')


def register_user(request):
    context = {}
    return render(request, 'authentication/register.html', context)
