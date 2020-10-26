from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.views import generic
from django.utils import timezone
from .models import Event, Info
from .forms import EventForm


# def index(request):
#    event = Event.objects.all()
#    context = {'all_event': event}
#    return render(request, 'kvent/index.html', context)
class IndexView(generic.ListView):
    """Show index view which is a list of all events."""

    template_name = 'kvent/index.html'
    context_object_name = 'all_event'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Event.objects.filter(event_name__contains=query)
        else:
            return Event.objects.all().order_by('-date_time')

def profile(request):
    """User's profile"""
    user = Info.objects.all()
    context = {user:'user'}
    return render(request, 'kvent/profile.html', context)


def create_event(request):
    """ User creates the event """
    form = EventForm(request.POST)
    if request.method == 'POST' :
        if form.is_valid() :
            event_name = form.data.get('event_name')
            location = form.data.get('location')
            short_description = form.data.get('short_description')
            long_description = form.data.get('long_description')
            number_people = form.data.get('number_people')
            event = Event(event_name = event_name, location=location,
             short_description = short_description, long_description = long_description
             , number_people = number_people,full=False)
            event.save()
            return redirect('index')
    return render(request, 'Kvent/create-event-page.html', {'form': form})