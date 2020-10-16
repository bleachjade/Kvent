from django.http import HttpResponse
from django.shortcuts import render
from .models import Info


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    """User's profile"""
    user = Info.objects.all()
    context = {user:'user'}
    return render(request, 'kvent/profile.html', context)