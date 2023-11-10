from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Usuario
from .serializers import UserSerializer
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
# Create your views here.

class UserView(APIView):
    def get(self, request):
        serializer = UserSerializer(Usuario.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            userName = data['usuario']
            password = data['pass']
            serializer = UserSerializer(Usuario.objects.get(nombre_usuario = userName, password_usuario = password))

            return JsonResponse(serializer.data)        
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Credenciales inválidas'}, status=400)
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)
        
    def put(self, request):
        try:
            data = JSONParser().parse(request)
            userName = data['usuario']
            newPassword = data['pass1']

            usuario = Usuario.objects.get(nombre_usuario = userName)

            usuario.password_usuario = newPassword;
            usuario.save()
            return JsonResponse({'mensaje': 'Contraseña cambiada exitosamente'})
        except Usuario.DoesNotExist:
            return  JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    



