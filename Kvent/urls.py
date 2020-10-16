from django.urls import path
from django.contrib import admin

from . import views
# from Kvent.views import LoginProjetView

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', LoginProjetView.as_view(), name='login'),
]