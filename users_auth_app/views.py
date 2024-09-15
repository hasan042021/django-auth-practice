from django.shortcuts import render, redirect
from .forms import RegisterForm, UserChangeForm
from django.contrib import messages
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    SetPasswordForm,
)
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.
def sign_up(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, "Account created successfully.")
                form.save()
        else:
            form = RegisterForm()
        return render(request, "auth.html", {"form": form, "type": "Sign Up"})
    else:
        return redirect("profile")


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data["username"]
            userpass = form.cleaned_data["password"]
            user = authenticate(username=name, password=userpass)
            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(request, "auth.html", {"form": form, "type": "Login"})


def user_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("homepage")


def password_change_with_old(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, "auth.html", {"form": form})
    else:
        return redirect("login")


def password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)
                return redirect("profile")
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, "auth.html", {"form": form})
    else:
        return redirect("login")


def profile(request):
    return render(request, "profile.html")
