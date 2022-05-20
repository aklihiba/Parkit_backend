from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ParkingSerializer, UserSerializer, ReservationSerializer
from .models import parkings, Utilisateur, Reservation

# Create your views here.

class ParkingViewSet(viewsets.ModelViewSet):
    queryset = parkings.objects.all().order_by('nom')
    serializer_class = ParkingSerializer

    
class UserViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UserSerializer

    @action(methods=['POST'], detail=True )
    def connexion(self, request, pk):
        email = request.data['email']
        mdp = request.data['mdp']
        print()
        try:
            user = Utilisateur.objects.get(userId = pk)
            ser = UserSerializer(data = user)
            if(user.email==email and user.mdp==mdp):
                return Response(ser.data)
            else:
                return Response('false credentials')    
        except Utilisateur.DoesNotExist:
           return Response('user not found')

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
          
    @action(methods=['GET'], detail=True )
    def UserReservation(self, request, pk):
    
        try:
            Reservations = Reservation.objects.all().filter(userId=pk)
            serializer = ReservationSerializer(instance = Reservations, context={'request': request}, many=True)
            
            return Response(serializer.data)
            
        except Reservation.DoesNotExist:
           return Response('this user has no reservations')      