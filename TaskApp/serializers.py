from rest_framework import serializers 
from rest_framework import fields
from .models import *


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model= Shift
        fields =['start_date','repeat','shifts','arrival_time','departure_time','weekdays','client_email']


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'email', 'first_name', 'last_name']

