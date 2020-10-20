from typing import Optional
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Info(models.Model):
    """User's model"""
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