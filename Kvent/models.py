# import datetime
from django.db import models
from datetime import datetime

myDate = datetime.now()
formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")
class Event(models.Model):
    """ Create the event """
    event_name = models.TextField('Event Name', default="", max_length=50)
    location = models.TextField('Location', default="", max_length=80)
    description = models.TextField('Description', default="", max_length=100)
    number_people = models.IntegerField("Number of people", default=2)
    date_time = models.TextField('Date and Time', default=str(formatedDate))

    def get_event_name(self):
        return self.event_name

    def get_location(self):
        return self.location
    
    def get_description(self):
        return self.description
    
    def get_time(self):
        return self.date_time
    
    def get_number_people(self):
        return self.number_people
