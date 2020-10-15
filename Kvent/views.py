from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def profile(request):
    """User's profile"""
    user = request.user
    info = request.user.info
    context = {'user':user, 'info':info}
    return render(request, 'BetterTogetherApp/profile.html', context)