from django.shortcuts import render
from rest_framework import generics
from api.serializers import UserSerializer,DonorSerializer
from django.contrib.auth.models import User
from api.models import Donor

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DonorList(generics.ListCreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer