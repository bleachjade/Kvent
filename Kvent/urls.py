from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

app_name = "kvent"
urlpatterns = [
    path('', views.index, name='index'),
    
]