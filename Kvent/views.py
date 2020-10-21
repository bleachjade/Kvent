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
    return render(request, 'registration/login.html')

def createaccount(request):
    return render(request, 'registration/createaccount.html')

