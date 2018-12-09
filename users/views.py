from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
        # View code here...
    return render(request, 'users/admin.html')

def logout(request):
    return HttpResponse("Logout")

def signup(request):
    return HttpResponse("sigup")
