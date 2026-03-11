from django.urls import path
from .views import registation_view

urlpatterns = [path("register/", registation_view.as_view(), name = "Registration")]