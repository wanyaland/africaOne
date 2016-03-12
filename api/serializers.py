__author__ = 'wanyama'
from rest_framework import serializers
from models import Donor
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        field=('id','username','password',)


class DonorSerializer(serializers.ModelSerializer):
    user = UserSerializer
    class Meta:
        model=Donor
        fields=('id','user','fine','fine_price','total_fine',)