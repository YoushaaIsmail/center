from rest_framework import serializers
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer

class Users2(UserDetailsSerializer):
    class Meta:
        model=User
        fields=['phone','name','address','photo','birthday','gender','email']        
