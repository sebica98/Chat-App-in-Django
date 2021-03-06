from time import strptime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User

from datetime import datetime

from ChatApp.forms import ImageForm
from .models import Profile, Message
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'index.html')

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
            #profile, created = Profile.objects.get_or_create(user=request.user)
            login(request, user)
            return redirect('/chatpage')

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
    return HttpResponse(f"Your username is {request.user.username} and your address: {request.user.profile.address}")

def logout_user(request):
    logout(request)
    return HttpResponse('Succesfully logged out!')

@login_required(login_url='/login')
def edit_user(request):
    if request.method == 'POST':
        user = request.user
        address = request.POST['address']
        image = request.FILES['photo']
        profile, created = Profile.objects.get_or_create(user=request.user)
        user.profile.address = address
        user.profile.photo = image
        user.save()
        return redirect('/chatpage')
    else:
        imageform = ImageForm()
        return render(request, "edituser.html", {'imageform': imageform})

@login_required(login_url='/login')
def chat_page(request):
    username = request.user
    return render(request, 'chatpage.html', {'username': username})

def send(request):
    message = request.POST['message']
    username = request.user
    new_message = Message.objects.create(content=message, author=username)
    new_message.save()
    return HttpResponse('Message was sent successfully')

def get_messages(request):
    messages = Message.objects.all()
    users = User.objects.values_list('username', 'id')
    profiles = Profile.objects.values_list('user_id', 'photo', 'slug')
    return JsonResponse({"messages": list(messages.values()),
                         "users": list(users),
                         "profiles": list(profiles)})


@login_required(login_url='/login')
def get_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    return render(request, "singleprofile.html", {
        "profile": profile,
    })