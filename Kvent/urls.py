from django.urls import path

from . import views

app_name = "kvent"
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/createaccount', views.createaccount, name='createaccount'),
    path('accounts/login', views.login, name='login'),
    path('accounts/display/createaccount', views.display_createaccount, name='display_createaccount'),
    path('accounts/display/login', views.display_login, name='display_login'),    
    # path('accounts/logout', views.logout, name='logout'),
]