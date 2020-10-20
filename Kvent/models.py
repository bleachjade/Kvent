# import datetime
from django.db import models
from datetime import datetime

myDate = datetime.now()
formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
class Event(models.Model):
    """ Create the event """
    event_name = models.TextField('Event Name', default="", max_length=50)
    location = models.TextField('Location', default="", max_length=80)
    short_description = models.TextField('Short Description', default="", max_length=100)
    long_description = models.TextField('Long Description', default="", max_length=255)
    number_people = models.IntegerField("Number of people", default=2)
    # date_time = models.TextField('Date and Time', default=str(formatedDate))
    # participants = models.ManyToManyField()
    full = models.BooleanField(default=False)

    def get_event_name(self):
        return self.event_name

    def get_location(self):
        return self.location
    
    def get_short_description(self):
        return self.short_description

    def get_long_description(self):
        return self.long_description
    
    def get_time(self):
        return self.date_time
    
    def get_number_people(self):
        return self.number_people

    def get_participants(self):
        return self.participants
    
    def get_full(self):
        return self.full
