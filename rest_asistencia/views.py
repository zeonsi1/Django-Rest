from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Usuario, Clase, Asignatura
from .serializers import UserSerializer, ClaseSerializer, AsignaturaSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from datetime import datetime
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

            usuario.password_usuario = newPassword
            usuario.save()
            return JsonResponse({'mensaje': 'Contraseña cambiada exitosamente'})
        except Usuario.DoesNotExist:
            return  JsonResponse({'error': 'Usuario no encontrado'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Error interno del servidor'}, status=500)

    
class ClaseView(APIView):
    def post(self, request):
        data = JSONParser().parse(request)
        id = data['id']
        clases = Clase.objects.filter(id_profesor=id).order_by('id_clase')
        serializer = ClaseSerializer(clases, many=True)
        
        asig = []
        for clase in clases:
            asignatura_id = clase.id_asignatura_id
            try:
                asignatura = Asignatura.objects.get(id_asignatura=asignatura_id)
                asig.append(asignatura)
            except Asignatura.DoesNotExist:
                pass

        asignatura_serializers = AsignaturaSerializer(asig, many=True)
        user = UserSerializer(Usuario.objects.get(id_profesor=id))

        combined_data = []
        for i in range(len(clases)):
            clase_data = {
                **serializer.data[i],
                **asignatura_serializers.data[i],
                **user.data,
            }
            combined_data.append(clase_data)


        return JsonResponse(combined_data, safe=False)
    
    def put(self, request):
        try:
            data = JSONParser().parse(request)
            id = data['id']
            date = data['fecha']
            total = data['total']

            if id is None or date is None or total is None:
                return JsonResponse({'mensaje': 'Parámetros faltantes'}, status=400)

            fecha = datetime.strptime(date, "%d/%m/%Y").strftime("%Y-%m-%d")
            clases = Clase.objects.get(id_clase=id)
            clases.fecha = fecha
            clases.total_clase += total
            clases.save()

            return JsonResponse({'mensaje': 'Fecha actualizada exitosamente'})
        except Clase.DoesNotExist:
            pass
    
class AsistenciaView(APIView):
    def put(self, request):
        try:
            data = JSONParser().parse(request)
            id = data['id']
            id_alumno = ['id_alumno']
            asis = ['asis']

        except:
            pass