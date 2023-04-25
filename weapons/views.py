from django.shortcuts import render
from rest_framework import generics
from .serializers import WeaponSerializer
from .models import Weapon
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .permissions import IsEmployee
from rest_framework_simplejwt.authentication import JWTAuthentication

class weaponView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]
    
    serializer_class = WeaponSerializer
  
    queryset = Weapon.objects.all()
    
    ...
class weaponDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]
    serializer_class = WeaponSerializer
  
    queryset = Weapon.objects.all()

    lookup_url_kwarg = 'weapon_id'