from django.shortcuts import render
from .models import Registration, Appointment
from .serializers import registration_serializer, Appointment_serializer
from rest_framework import generics

# Create your views here.
class registation_view(generics.ListCreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = registration_serializer

class Appointment_view(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = Appointment_serializer

