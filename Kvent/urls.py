from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url



urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:event_id>/', views.detail, name='event-detail'),
    path('accounts/profile/', views.profile, name='profile'),
    path('create',views.create_event, name='create-event'),
    path('delete/<int:event_id>', views.delete_event, name='delete-event'),
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
] 
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

