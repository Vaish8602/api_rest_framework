from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    class Meta:
        model = Client
        fields = ['id', 'name', 'created_by', 'created_at', 'updated_at']

class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.ReadOnlyField(source='client.name')
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id', 'name', 'client', 'users', 'created_at', 'updated_at']
