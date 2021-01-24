from rest_framework import serializers 
from rest_framework import fields
from .models import *
import datetime

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model= Shift
        fields =['start_date','repeat','shifts','arrival_time','departure_time','weekdays']
    def validate(self, data):
        if "departure_time" in data and "arrival_time" in data:
            if data["departure_time"] < data["arrival_time"]:
                raise serializers.ValidationError({
                    "departure_time": "Departure time cannot be less than Arrival time",
                })

        return super(ShiftSerializer, self).validate(data)


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'email', 'username','first_name', 'last_name']


class ShiftListSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('get_username_from_client')
    class Meta:
        model= Shift
        fields =['start_date','repeat','shifts','arrival_time','departure_time','weekdays','email']
    def get_username_from_client(self, shift_post):
        email = shift_post.client.email
        return email