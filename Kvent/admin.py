from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = (
        'event_name',
        'location',
        'short_description'
    )


admin.site.register(Event, EventAdmin)
