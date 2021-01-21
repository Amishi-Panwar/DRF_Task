from django.db import models
import datetime
from datetime import timedelta
from django.utils import timezone
from multiselectfield import MultiSelectField
from django import forms
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import ClientManager
from django.contrib .auth.models import User
CHOICES = [
        ('None', 'None'),
        ('Daily', 'Daily'), 
        ('Weekly','Weekly')
]
SHIFTS=[
    ('Morning Shift - 5am to 9am','Morning Shift - 5am to 9am')
]

WEEKDAYS = [
        ('Sunday','SUN'),
        ('Monday','MON'),
        ('Tuesday','TUE'),
        ('Wednesday','WED'),
        ('Thursday','THUS'),
        ('Friday','FRI'),
        ('Saturday','SAT'),
]

class Client(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = ClientManager()

    def __str__(self):
        return self.email

def default_start_time():
    now = datetime.now()
    start = now.replace(hour=22, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)  


class Shift(models.Model):
    start_date=models.DateField()
    repeat= models.CharField(max_length=6,choices=CHOICES,default=None)
    shifts=models.CharField(max_length=50, choices =SHIFTS,default='Morning Shift - 5am to 9am')
    arrival_time=models.TimeField(default=datetime.datetime.strptime('08:00', '%H:%M').time(), blank = True, null = True)
    departure_time=models.TimeField(default=datetime.datetime.strptime('08:00', '%H:%M').time())
    weekdays=MultiSelectField(max_choices=7,choices=WEEKDAYS,default='ONE')
    client_email= models.ForeignKey(Client, on_delete=models.CASCADE,default="")
