from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_name',
        'location',
        'short_description'
    )
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'activity_name'
        'description'
    )

admin.site.register(Event, EventAdmin)
admin.site.register(Activity, ActivityAdmin)
