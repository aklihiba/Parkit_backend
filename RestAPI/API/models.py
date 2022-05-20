from django.db import models

# Create your models here.

class parkings(models.Model):
    id = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=256, null=False,blank=False)
    adresse = models.CharField(max_length=256,null=False,blank=False)
    latitude = models.FloatField()
    longitude = models.FloatField()
    etat = models.CharField(max_length=20)
    note = models.FloatField()
    heure_ouverture = models.DurationField()
    heure_fermeture = models.DurationField()
    tarif = models.FloatField()
    occupation = models.FloatField()
    nombre_places = models.IntegerField()
    photo = models.CharField(max_length=512)

    def __str__(self):
        return self.nom

class Utilisateur(models.Model):
    userId = models.IntegerField(primary_key=True)
    nom = models.CharField(max_length=60)
    prenom = models.CharField(max_length=60)
    email = models.CharField(max_length=256)
    tel = models.CharField(max_length=10)
    mdp = models.CharField(max_length=256)
    photo = models.CharField(max_length=512, blank=True)

    def __str__(self) -> str:
        return self.email

class Reservation(models.Model):
    ReservationId = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(Utilisateur, on_delete=models.CASCADE,default=None)
    parkingId = models.ForeignKey(parkings, on_delete=models.CASCADE,default=None)
    hEntree = models.DateTimeField()
    hSortie = models.DateTimeField()
    code_QR = models.CharField(max_length=512, blank=True) #link to the QR image
    num_place = models.CharField(max_length=10)
    prix = models.FloatField(default=100.0, blank= True)
    def __str__(self) -> str:
        return '{} {} {}'.format(str(self.id),str(self.user_id), str(self.parking_id))