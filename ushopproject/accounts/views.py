from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == "POST":
        try:
            if request.POST["password1"] == request.POST["password2"]:
                user = User.objects.get(username=request.POST["login"])
                return render(request, "accounts/signup.html", {"error": "Username have already been taken"})
        except User.DoesNotExist:
            user = User.objects.create_user(username=request.POST["login"], password=request.POST["password1"])
            auth.login(request, user)
            return redirect('home')

    else:
        return render(request, "accounts/signup.html")


def login(request):
    return render(request, "accounts/login.html")


def logout(request):
    return render(request, "accounts/signup.html")
