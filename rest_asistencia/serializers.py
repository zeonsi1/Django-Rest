from rest_framework import serializers
from core.models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['id_usuario', 'nombre_usuario', 'direccion_usuario', 'password_usuario', 'pnombre_usuario', 'apaterno_usuario']