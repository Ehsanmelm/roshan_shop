from rest_framework import serializers 
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer
from .models import User


class UserRegisterSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ['id' , 'username' ,'password' , 'email','first_name' , 'last_name'] 
        extra_kwargs = {'password' : {'write_only' : True} }




class UserLoginSerializer(ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields= ['id','username' , 'password']