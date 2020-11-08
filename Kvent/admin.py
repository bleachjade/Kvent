from django.contrib import admin
from .models import *
class EventAdmin(admin.ModelAdmin):
    """Model for display event infomation in admin page"""
    list_display = (
        'event_name',
        'location',
        'short_description'
    )
class UserAdmin(admin.ModelAdmin):
    """Model for display user infomation in admin page"""
    list_display = (
        'username',
        'email',
    )

admin.site.register(Event,EventAdmin)
admin.site.register(User, UserAdmin)
