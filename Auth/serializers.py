from rest_framework import serializers 
from .models import Registration

class registration_serializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['First_name', 'Second_name', 'Email']

    
 