from django.db import models
import datetime
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import ClientManager
from django.contrib.auth.models import User
from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

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

class Shift(models.Model):
    start_date=models.DateField(blank = False)
    repeat= models.CharField(max_length=6,choices=CHOICES,default='None',blank = False,null=True)
    shifts=models.CharField(max_length=50, choices =SHIFTS,default='Morning Shift - 5am to 9am',blank = False)
    arrival_time=models.TimeField(default=datetime.datetime.strptime('05:00', '%H:%M').time(), blank = False)
    departure_time=models.TimeField(default=datetime.datetime.strptime('09:00', '%H:%M').time(),blank = False)
    weekdays=MultiSelectField(max_choices=7,choices=WEEKDAYS,blank = False)
    client= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

