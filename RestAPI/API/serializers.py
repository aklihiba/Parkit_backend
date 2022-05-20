# serializers.py
from dataclasses import field, fields
from rest_framework import serializers

from .models import parkings, Utilisateur, Reservation

class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parkings
        fields ='__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Utilisateur
        fields = '__all__'

    
class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
