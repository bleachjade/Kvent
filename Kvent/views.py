from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, Info

def index(request):
   event = Event.objects.all()
   return render(request, 'kvent/index.html', {'all_event': event})

def create(request):
    return render(request, 'kvent/create-event-page.html')
  
def profile(request):
    """User's profile"""
    user = Info.objects.all()
    return render(request, 'kvent/profile.html',{user:'user'})

def detail(request, event_id):
   event = get_object_or_404(Event, pk=event_id)
   return render(request, 'kvent/event-detail.html', {'event': event})