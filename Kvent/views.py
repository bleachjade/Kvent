from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, FormView
from django.contrib.auth.models import User
from django.views import generic, View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
# from .forms import UserRegistrationForm, EventForm, AddQuestion
from .models import *
import datetime

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    """
    If the user is not authenticated, get user's request and execute login.
    """
    # if request.method == "POST":
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return HttpResponseRedirect(reverse('myform:event'))
    #     else:
    #         messages.error(request, 'Wrong username or password try again!')
    #         return render(request, 'registration/login.html')
    # else:
    return render(request, 'kvent/login.html')
