from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Event, Info, User
from .forms import EventForm,SignUpForm
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

class IndexView(generic.ListView):
    """Show index view which is a list of all events."""

    template_name = 'kvent/index.html'
    context_object_name = 'all_event'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            return Event.objects.filter(event_name__contains=query)
        else:
            return Event.objects.all().order_by('-date_time')

@login_required(login_url='login/')
def profile(request):
    """User's profile"""
    user = Info.objects.all()
    return render(request, 'kvent/profile.html',{user:'user'})

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user
    return render(request, 'kvent/event-detail.html', {'event': event, 'user': user})

@login_required(login_url='login')
def create_event(request):
    """ User creates the event """
    form = EventForm(request.POST, request.FILES)
    if request.method == 'POST' :
        if form.is_valid() :
            photo = form.cleaned_data.get('photo') 
            event_name = form.data.get('event_name')
            location = form.data.get('location')
            short_description = form.data.get('short_description')
            long_description = form.data.get('long_description')
            number_people = form.data.get('number_people')
            event = Event(event_name = event_name, location=location,
             short_description = short_description, long_description = long_description
             , number_people = number_people,full=False, photo=photo, user=request.user)
            event.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'Kvent/create-event-page.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            email = form.data.get('email')
            username = form.data.get('username')
            raw_password = form.data.get('raw_password')
            user = authenticate(email=email,username=username, password=raw_password)
            form.save()
            return redirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request,'registration/createaccount.html', {'form': form})

@login_required(login_url='/login/')
def delete_event(request, event_id):
    event = Event.objects.get( pk=event_id)
    event.delete()
    return redirect('index')

@login_required
def join_event(request, event_id):
    user = request.user.id
    try:
        event = get_object_or_404(Event, pk=event_id)
    except (KeyError, Event.DoesNotExist):
        return redirect('index')
    else:
        event.participants.add(user)
    return redirect('index')

@login_required
def leave_event(request, event_id):
    user = request.user.id
    try: 
        event = get_object_or_404(Event, pk=event_id)
    except (KeyError, Event.DoesNotExist):
        return redirect('index')
    else:
        event.participants.remove(user)
    return redirect('index')

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('index')
