from rest_framework import serializers
from core.models import User
from core.models import Usuario

from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['tipo_usuario', 'pnombre_usuario', 'apaterno_usuario']


