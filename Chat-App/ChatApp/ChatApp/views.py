from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

def home(request):
    return render(request,'index.html')

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponse("Unauthorized")
    return HttpResponse("<h1>Dashboard</h1>")

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if (username == ""): return HttpResponse("No username!")
        if (password == ""): return HttpResponse("No password!")
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse("Unauthorized")
        else:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if (username == ""): return HttpResponse("No username!")
        if (password == ""): return HttpResponse("No password!")
        if (email == ""): return HttpResponse("No email!")
        User.objects.create_user(username=username, password=password, email=email)
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('Unauthorized')
        else:
            #login(request, user)
            return redirect('/')
    return render(request, 'signup.html')

def username(request):
    return HttpResponse(f"Your username is {request.user.username}")

def logout_user(request):
    logout(request)
    return HttpResponse('Succesfully logged out!')