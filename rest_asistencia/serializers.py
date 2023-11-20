from rest_framework import serializers
from core.models import Usuario, Clase



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'tipo_usuario', 'pnombre_usuario', 'apaterno_usuario']

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'
