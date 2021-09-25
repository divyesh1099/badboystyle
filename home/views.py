from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from .models import *

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def all(request):
    return render(request, 'home/all.html')

def gallery(request):
    return render(request, 'home/gallery.html')

def categories(request):
    return render(request, 'home/categories.html')

def my_login(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return render(request, 'home/index.html', {'success': "Logged in Successfully"})
        else:
            return render(request, "home/login.html", {
                "error": "Invalid username and/or password."
            })
    else:
        return render(request, "home/login.html")

def my_logout(request):
    logout(request)
    return render(request, 'home/index.html', {'success': "Logged Out Successfully"})

def my_signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password1"]
        confirmation = request.POST["password2"]
        if password != confirmation:
            return render(request, "home/signup.html", {
                "error": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_superuser(username, email, password)
            user.set_password(password)
            user.is_active=True
            user.save()
        except IntegrityError:
            print("Error")
            return render(request, "home/signup.html", {
                "error": "Username already taken."
            })
        login(request, user)
        return render(request, 'home/index.html', {"success": "Logged In Successfully"})
    else:
        return render(request, "home/signup.html")