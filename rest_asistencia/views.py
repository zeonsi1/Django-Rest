from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Usuario
from .serializers import UsuarioSerializer
from rest_framework import status
from django.contrib.auth import authenticate
# Create your views here.

class UserView(APIView):
    def get(self, request):
        serializer = UsuarioSerializer(Usuario.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        username = request.data.get('usuario')
        password = request.data.get('pass')
        serializer = Usuario.objects.filter(nombre_usuario = username)
        return Response(serializer.data)

        

    



