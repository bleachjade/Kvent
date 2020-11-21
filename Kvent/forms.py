from django import forms
from .models import Event, User
from django.forms.widgets import Textarea
from Kvent.models import User
from django.contrib.auth.forms import UserCreationForm

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
            widget=forms.NumberInput(
            attrs={'type':'number', 'id':'number-people'}
            ))
        photo = forms.ImageField()



class SignUpForm(UserCreationForm):
    """ Form for create a new account """
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ( 'email','username', 'password1')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),
        }
