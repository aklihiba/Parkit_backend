# serializers.py
from dataclasses import field, fields
from rest_framework import serializers

from .models import parkings

class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = parkings
        fields = ('id','nom', 'adresse','latitude', 'longitude','etat','note','heure_ouverture',
                    'heure_fermeture', 'tarif', 'occupation', 'nombre_places', 'photo')

# use it for inscription and getting the user info  
# class UserSerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model  = User
#         fields = ('id', 'nom', 'prenom', 'email', 'photo','password', 'tel')

# class ReservationSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Reservation
#         fields = ('reservationId', 'userId','parkingId','hEntree', 'hSortie','code_QR','num_place')
