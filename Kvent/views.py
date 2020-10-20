from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Event, Info

def index(request):
   event = Event.objects.all()
   context = {'all_event': event}
   return render(request, 'kvent/index.html', context)

def create(request):
    return render(request, 'kvent/create-event-page.html')
  
def profile(request):
    """User's profile"""
    user = Info.objects.all()
    context = {user:'user'}
    return render(request, 'kvent/profile.html', context)