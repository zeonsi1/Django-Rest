from rest_framework import serializers
from core.models import User

from django.contrib.auth import authenticate

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['tipo_usuario', 'first_name', 'last_name','username', 'password', ]
