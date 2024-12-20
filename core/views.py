from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status 
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import UserRegisterSerializer, UserLoginSerializer 
from .models import User

# Create your views here.

class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer
    
    def post(self,request):
        serializer = UserRegisterSerializer(data =request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        user.set_password(user.password)
        user.save()
        token , created = Token.objects.get_or_create(user=user)

        context= {
            'user' : serializer.data,
            'Token' : token.key
        }

        return Response(context , status=status.HTTP_200_OK)
    

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer

    def post(self,request):
        serializer = UserLoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        username = request.data['username']
        password = request.data['password'] 
        user= authenticate(username=username , password=password)

        if not user:
            raise ValidationError("Invalid credentials", status.HTTP_401_UNAUTHORIZED)
        
        token , created = Token.objects.get_or_create(user = user)
        context = {
            'username' : user.username,
            'email' : user.email,
            'Token' : token.key
        }
        return Response(context , status= status.HTTP_200_OK)

        # try:
            # user = User.objects.get(username = request.data['username'] , password = request.data['password'] )
            # token , created = Token.objects.get_or_create(user = user)

            # context = {
            #     'username' : user.username,
            #     'email' : user.email,
            #     'Token' : token.key
            # }
            # return Response(context , status= status.HTTP_200_OK)
            
        # except:
            # raise ValidationError("User Not Found ", status.HTTP_400_BAD_REQUEST)
        

class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        token = Token.objects.get(user = request.user)
        token.delete()

        return Response("log out successfully " , status=status.HTTP_200_OK)