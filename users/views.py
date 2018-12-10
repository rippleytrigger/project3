from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.models import User

  # Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout(request):
    auth_logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def signup(request):
    username = request.POST["username"]
    password = request.POST["password"]
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    email = request.POST["email"]

    return render(request, 'users/sigup.html')
