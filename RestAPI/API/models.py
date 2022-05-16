from pickle import TRUE
from django.db import models

# Create your models here.

class Parking(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=256, null=False,blank=False)
    adresse = models.CharField(max_length=256,null=False,blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    ouvert = models.BooleanField()
    note = models.FloatField()
    horaire_debut = models.DurationField()
    horaire_fin = models.DurationField()
    prix = models.FloatField()
    taux_occupation = models.FloatField()
    nombre_places = models.IntegerField()

    def __str__(self):
        return self.nom