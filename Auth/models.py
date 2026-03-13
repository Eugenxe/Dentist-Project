from django.db import models

class Registration(models.Model):
    First_name = models.CharField(max_length=50)
    Second_name = models.CharField(max_length=50)
    Email = models.EmailField(unique=True)

#Include Id number


class Appointment(models.Model):
    patient = models.ForeignKey(Registration, on_delete=models.CASCADE)
    date = models.DateField(default='2026-03-20')
    
    

