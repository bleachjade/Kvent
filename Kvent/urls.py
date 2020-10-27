from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:event_id>/', views.detail, name='event-detail'),
    path('profile', views.profile, name='profile'),
    path('create',views.create_event, name='create-event'),
    path('delete/<int:event_id>', views.delete_event, name='delete-event'),
]

