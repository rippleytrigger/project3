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
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        if len(username) == 0:
            return render(request, 'users/login.html', {"message": "Please put a valid username"})

        try:
            User.objects.get(username=username)
        except Exception:
            return render(request, 'users/login.html', {"message": "That User Does not Exists!"})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "users/login.html")

def logout(request):
    auth_logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def signup(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        if password != password2:
            return render(request, 'users/sigup.html', {"message": "The Password confirmation should match your password."}) 
        
        if User.objects.filter(username=username).exists():
            return render(request, 'users/sigup.html', {"message": "The username already exists. Please choose another one."})

        try:
            user = User.objects.create_user(username = username, password = password, first_name = first_name, last_name = last_name, email = email)
        except Exception as e: 
            return render(request, 'users/sigup.html', {"message": e})

        user.save()

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, 'users/sigup.html')
