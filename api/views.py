from django.shortcuts import render
from rest_framework import generics
from api.serializers import UserSerializer,DonorSerializer
from django.contrib.auth.models import User
from api.models import Donor
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DonorList(generics.ListCreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer

class DonorDetail(APIView):

    def get_object(self,pk):
        try:
            return Donor.objects.get(pk=pk)
        except Donor.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        donor = self.get_object(pk)
        donor = DonorSerializer(donor)
        return Response(donor.data)

    def put(self,request,pk,format=None):
        donor = self.get_object(pk)
        serializer = DonorSerializer(donor,data=request.DATA)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        donor = self.get_object(pk)
        donor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


