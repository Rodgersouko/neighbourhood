from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import *
from django.contrib.auth import login
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from . models import *
# Create your views here.


def home(request):
    return HttpResponse("WELCOME TO MY HOOD......")



class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
###########################################################################


class NeighbourhoodViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing neighborhood instances.
    """
    serializer_class = NeighbourhoodSerializer
    queryset = Neighbourhood.objects.all()


class ProfileViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()


class BusinessViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = BusinessSerializer
    queryset = Business.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing profile instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class IsAssigned(permissions.BasePermission):
    """
    Only person who assigned has permission
    """

    def has_object_permission(self, request, view, obj):
	# check if user who launched request is object owner
        if obj.assigned_to == request.user:
            return True
        return False


class IsReadOnlyOrIsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        authenticated = request.user.is_authenticated
        if not authenticated:
            if view.action == '/':
                return True
            else:
                return False
        else:
            return True


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
