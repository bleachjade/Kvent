from django.shortcuts import render, redirect
from .models import Event

def index(request):
   event = Event.objects.all()
   context = {'all_event': event}
   return render(request, 'kvent/index.html', context)

def create(request):
    return render(request, 'kvent/create-event-page.html')