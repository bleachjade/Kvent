from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, FormView
from django.contrib.auth.models import User
from django.views import generic, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm



# from .forms import UserRegistrationForm, EventForm, AddQuestion
from .models import *
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username = username)
            if user.password == password:
                return HttpResponse("Yess")
            else:
                return HttpResponse("pass Nooo")
        except User.DoesNotExist:
            return HttpResponse("user Nooo")
    

def display_login(request):
    return render(request, 'registration/login.html')

def display_createaccount(request):
    return render(request, 'registration/createaccount.html')

def createaccount(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User(email = email, username = username, password = password)
        user.save()
    return redirect('kvent:display_login')
    



