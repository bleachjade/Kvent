from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views

app_name = "kvent"
urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/createaccount', views.create_account, name='createaccount'),
    # path('accounts/login', views.login, name='login'),
    # path('accounts/display/createaccount', views.display_create_account, name='display_createaccount'),
    # path('accounts/display/login', views.display_login, name='display_login'),    
    # path('accounts/logout', views.logout, name='logout'),
]