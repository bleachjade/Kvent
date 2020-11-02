from django import forms
from .models import Event
from django.forms.widgets import Textarea

class EventForm(forms.ModelForm):
    """ Form for inputing a new event """
    class Meta:
        model = Event
        fields = ['event_name','location', 'short_description', 'long_description', 'number_people', 'photo']
        event_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'name-input'}
            ))
        location = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'location-input'}
            ))
        short_description = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'short-description-input'}
            ))
        long_description = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'long-description-input'}
            ))
        number_people = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'number-people'}
            ))
        photo = forms.ImageField()
