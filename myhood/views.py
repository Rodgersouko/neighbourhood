from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework import generics, permissions, status
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from knox import views as knox_views
from .serializers import *

# Create your views here.
# def home(request):
#     return HttpResponse("Hello world")


# CreateUserSerializerAPI

class CreateUserSerializer(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.data
        # user = request.user
        context = {
            "user": serializer.data,
            "status": status.HTTP_201_CREATED,
            "token": AuthToken.objects.create(user)[1]
        }
        return Response(context)

class LoginUserSerializer(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        context = {
            "user": serializer.data,
            "token": AuthToken.objects.create(user)[1]
        }
        return Response(context)


    
