# serializers.py
from rest_framework import serializers

from .models import Parking

class ParkingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Parking
        fields = ('id','nom', 'adresse','latitude', 'longitude','ouvert','note','horaire_debut',
                    'horaire_fin', 'prix', 'taux_occupation', 'nombre_places')
  