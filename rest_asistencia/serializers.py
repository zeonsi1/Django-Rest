from rest_framework import serializers
from core.models import Usuario, Clase, Asignatura



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'tipo_usuario', 'pnombre_usuario', 'apaterno_usuario', 'id_profesor', 'mail_usuario']
        safe = False

class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'
        safe = False

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'
        safe = False