from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .serializers import * 
from .models import *
from rest_framework.generics import ListCreateAPIView   
from .models import *


class ShiftView(ListCreateAPIView):   
    serializer_class = ShiftSerializer       
    queryset = Shift.objects.all()  

    def perform_create(self, serializer):
        serializer.save(client_email=self.request.user)
    
class ClientView(ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    