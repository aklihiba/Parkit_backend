from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ParkingSerializer
from .models import Parking

# Create your views here.

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = Parking.objects.all().order_by('nom')
    serializer_class = ParkingSerializer
