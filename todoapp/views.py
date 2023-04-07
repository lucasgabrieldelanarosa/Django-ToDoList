from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from .models import *

# Create your views here.

def home(request):
    currentUser = request.user 
    allProjects = Project.objects.filter(user=currentUser)
    
    return render(request, 'todoapp/index.html', {
        'currentUser': currentUser,
        'allProjects': allProjects
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["userName"]
        password = request.POST["userPassword"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "todoapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "todoapp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):    
    if request.method == "POST":
        username = request.POST["userName"]
        email = request.POST["userEmail"]

        # Ensure password matches confirmation
        password = request.POST["userPassword"]
        confirmation = request.POST["checkPassword"]
        if password != confirmation:
            return render(request, "todoapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "todoapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "todoapp/register.html")
    

def create(request):
    return render(request, 'todoapp/create.html')


def create_project(request):
    return render(request, 'todoapp/create_project.html')


def create_task(request):
    currentUser = request.user
    allProjects = Project.objects.filter(user=currentUser)
    allPriorities = Priority.objects.all()

    return render(request, 'todoapp/create_task.html', {
        'allProjects': allProjects,
        'allPriorities': allPriorities,
    })

