from rest_framework import serializers
from core.models import Usuario

from django.contrib.auth import authenticate

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['id_usuario', 'tipo_usuario', 'nombre_usuario', 'password_usuario', 'pnombre_usuario', 'apaterno_usuario']
