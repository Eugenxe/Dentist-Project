from django.contrib import admin
from .models import Appointment, Registration

# Register your models here.
admin.site.register(Registration)
admin.site.register(Appointment)