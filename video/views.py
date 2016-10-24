from django.shortcuts import render, redirect
from .models import Video
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http.response import HttpResponse
from .forms import LoginForm


def home(request):
    videos = Video.objects.all().order_by('-title')
    return render(request, 'home.html', {'videos': videos})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = form.authenticate()
        if user:
            return HttpResponse("Successful")
        else:
            return HttpResponse("Login Failed")
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})


        # username = request.POST.get('username', None)
        # password = request.POST.get('password', None)
        # if username and password:
        #     user = authenticate(username=username, password=password)
        #     if user:
        #         return HttpResponse("Successful")
        #     else:
        #         return HttpResponse("Login Failed")
        # else:
        #     return HttpResponse("Empty input detected")


def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                return HttpResponse("User id "+ str(user.id) + " created")
            else:
                return HttpResponse("Something Went Wrong")
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})