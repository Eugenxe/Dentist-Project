from django.shortcuts import render
from .models import Registration
from .serializers import registration_serializer
from rest_framework import generics

# Create your views here.
class registation_view(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = registration_serializer



