from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Model for put the user account to databasel"""
    email = models.EmailField("E-mail", max_length=254)
    # username = models.CharField("Username", max_length=254)
    # raw_password = models.CharField("Password", max_length=254)

class Info(models.Model):
    """Model for put the user's infomation to databasel"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True, default=None)
    phone_num = models.CharField('Phone Number', max_length=10, default="NOT SET")
    email = models.EmailField('E-mail', max_length=254)
    address = models.CharField("Address", max_length=125, default="NOT SET")


    def get_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_number(self):
        return self.phone_num

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address
      
myDate = datetime.now()
formatedDate = myDate.strftime("%Y-%m-%d %H:%M:%S")

class Event(models.Model):
    """ Model for put the infomation of event to database """
    event_name = models.TextField('Event Name', default="", max_length=50)
    location = models.TextField('Location', default="", max_length=80)
    short_description = models.TextField('Short Description', default="", max_length=100)
    long_description = models.TextField('Long Description', default="", max_length=255)
    number_people = models.IntegerField("Number of people", default=2)
    date_time = models.DateTimeField('Date and Time', default=timezone.now)
    photo = models.ImageField(upload_to='upload/', default='upload/images/no_img.png', null=True)
    # participants = models.ManyToManyField(Info)
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

    def get_photo(self):
        return self.photo

