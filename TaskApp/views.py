from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from .serializers import * 
from .models import *
from rest_framework.generics import ListCreateAPIView   
from .models import *
from django.contrib.auth import login, authenticate

class ShiftView(ListCreateAPIView):   
    serializer_class = ShiftSerializer      
    queryset = Shift.objects.all()
    def perform_create(self, serializer):
        serializer.save(client=self.request.user)
    
class ClientView(ListCreateAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    
class ShiftListView(ListCreateAPIView):
    serializer_class = ShiftListSerializer
    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return ("auth")
        return Shift.objects.filter(client=user)
