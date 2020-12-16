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
from django.utils import timezone
import datetime
import sys

class IndexView(generic.ListView):
    """Show index view which is a list of all events and render index page."""

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
    """Function for render user's profile page."""
    user = Info.objects.all()
    return render(request, 'kvent/profile.html',{user:'user'})

def detail(request, event_id):
    """Function for render event detail page."""
    event = get_object_or_404(Event, pk=event_id)
    user = request.user
    return render(request, 'kvent/event-detail.html', {'event': event, 'user': user})

@login_required(login_url='login')
def event_history(request, username):
    user = request.user
    event_host = Event.objects.filter(user=user)
    event_participant = Event.objects.filter(participants=user)
    return render(request, 'kvent/event-history.html', {
        'user': user, 
        'event_host': event_host,
        'event_participant': event_participant
        })

@login_required(login_url='login')
def create_event(request):
    """ 
    Function for create event with form and only logged in user can create the event 
    and render create event page.
    """
    form = EventForm(request.POST, request.FILES)
    number_people = form.data.get('number_people')
    arrange_time = form.data.get('arrange_time')
    if request.method == 'POST':
        if form.is_valid():
            if int(number_people) >= 10:
                try:
                    if datetime.datetime.strptime(arrange_time,'%Y-%m-%d %H:%M').date() > timezone.now().date():
                        photo = form.cleaned_data.get('photo') 
                        event_name = form.data.get('event_name')
                        location = form.data.get('location')
                        short_description = form.data.get('short_description')
                        long_description = form.data.get('long_description')
                        event = Event(event_name = event_name, location=location, short_description = short_description, long_description = long_description, arrange_time = arrange_time, number_people = number_people,full=False, photo=photo, user=request.user)
                        event.save()
                        messages.success(request, f"You've created the {event_name} event!")
                        return HttpResponseRedirect(reverse('index'))
                    else:
                        messages.warning(request, "Arrangement date must be in the future!")
                except:
                    messages.warning(request, f"You should input the date and time as format!")
                    return render(request, 'Kvent/create-event-page.html', {'form': form})
            else :
                messages.warning(request, "Number of paricipants must more than 10 or equal")
        else:
            messages.warning(request, f"You should input the date and time as format!")
    return render(request, 'Kvent/create-event-page.html', {'form': form})

def signup(request):
    """Function for let user who doesn't have an account to create an account and render signup page."""
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            email = form.data.get('email')
            username = form.data.get('username')
            if User.objects.filter(username=username).exists():
                messages.error(request, "Your username is already taken!")
                form = SignUpForm()
            else:  
                raw_password = form.data.get('raw_password')
                user = authenticate(email=email,username=username, password=raw_password)
                form.save()
                return redirect(reverse('login'))
    else:
        form = SignUpForm()
    return render(request,'registration/createaccount.html', {'form': form})

@login_required(login_url='/login/')
def delete_event(request, event_id):
    """Function for delete event and only logged in user can delete event."""
    DANGER = 50
    event = Event.objects.get( pk=event_id)
    if str(request.user) == event.user:
        messages.add_message(request, DANGER, f"You've deleted the {event.event_name} event.", extra_tags='danger')
        event.delete()
    else:
        messages.warning(request, "You can only delete your event.")
        return redirect('index')
    return redirect('index')

@login_required(login_url='/login/')
def join_event(request, event_id):
    user = request.user.id
    try:
        event = get_object_or_404(Event, pk=event_id)
    except (KeyError, Event.DoesNotExist):
        return redirect('index')
    else:
        if str(request.user) == event.user:
            messages.warning(request, f"You can't join your own event!")
            return redirect('index')
        else:
            messages.success(request, f"You've joined the {event.event_name} event!")
            event.participants.add(user)
    return redirect('index')

@login_required(login_url='/login/')
def leave_event(request, event_id):
    DANGER = 50
    user = request.user.id
    try: 
        event = get_object_or_404(Event, pk=event_id)
    except (KeyError, Event.DoesNotExist):
        return redirect('index')
    else:
        messages.add_message(request, DANGER, f"You've left the {event.event_name} event.", extra_tags='danger')
        event.participants.remove(user)
    return redirect('index')

@login_required(login_url='login')
def logout(request):
    logout(request)
    return redirect('index')

def view404(request, exception):
    res = render(request, 'Kvent/404.html')
    res.status_code = 404
    return res