from django.contrib import admin
from .models import  Utilisateur, parkings, Reservation


# Register your models here.
admin.site.register(parkings)
admin.site.register(Utilisateur)
admin.site.register(Reservation)