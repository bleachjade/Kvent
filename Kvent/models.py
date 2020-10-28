
from typing import Optional
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django import forms

class User(models.Model):
    """User's model"""
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=254)
    password = models.CharField(max_length=254)
    

