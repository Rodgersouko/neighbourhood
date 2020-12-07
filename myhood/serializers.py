from rest_framework import generics, permissions, serializers, exceptions
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets


class UserSerializer(serializers.ModelSerializer):
    # neighbourhood = serializers.CharField(source='neighbourhood.name')
    class Meta:
        model = User
        fields = ['first_name', 'email', 'is_staff', 'last_name', 'avatar']

    def create(self, validated_data):
        validated_data['password'] = make_password(
            validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
# Register Serializer


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
           validated_data['email'], validated_data['password'])
        return user


class ChangePasswordSerializer(serializers.Serializer):
    model = User
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    ############################################################


class NeighbourhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbourhood
        fields = ('id', 'name', 'location', 'admin', 'occupantsCount', 'image')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name', 'email', 'status', 'image', 'user')


class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ('id', 'business_name', 'user', 'neighbourhood',
                  'business_email', 'business_profile')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'neighbourhood', 'text', 'image')
