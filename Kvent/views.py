from django.shortcuts import render, redirect

def index(request):
   return render(request, 'kvent/index.html')

def create(request):
    return render(request, 'kvent/create-event-page.html')