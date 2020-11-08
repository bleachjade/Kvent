from django.contrib import admin
from .models import *
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_name',
        'location',
        'short_description'
    )
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
    )

admin.site.register(Event,EventAdmin)
admin.site.register(User, UserAdmin)
