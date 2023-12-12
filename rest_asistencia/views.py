from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Usuario, Clase, Asignatura
from .serializers import UserSerializer, ClaseSerializer, AsignaturaSerializer
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http import JsonResponse, HttpResponseServerError
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
        try:
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
        except:
            pass
    
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
            id_alumno = data['idAlumno']
            asis = data['asis']
            fecha = data['fecha']
            hora = data['hora']
            if id is None or fecha is None or asis is None:
                return JsonResponse({'mensaje': 'Parámetros faltantes'}, status=400)

            fecha = datetime.strptime(fecha, "%d/%m/%Y").strftime("%Y-%m-%d")

            clases = Clase.objects.get(id_usuario=id_alumno, id_clase = id)
            clases.fecha = fecha
            clases.hora = hora
            clases.clase_asistida += asis
            clases.save()
            
            id_asig = clases.id_asignatura_id

            asig = Asignatura.objects.get(id_asignatura = id_asig)

            nombre_asignatura = asig.nombre_asignatura

            id_profesor = clases.id_profesor_id

            correo = Usuario.objects.get(id_profesor = id_profesor)

            correo = correo.mail_usuario

            self.enviar_correo_asistencia(id_alumno, fecha, hora, correo, id, nombre_asignatura)
            return JsonResponse({'mensaje': 'Asistencia registrada!'})
        except Usuario.DoesNotExist:
            return  JsonResponse({'error': 'Usuario no es de esta clase'}, status=404)
        except Exception as e:
            print(f'Error en la vista: {repr(e)}')
            return JsonResponse({'error': str(e)}, status=400)
        
    def enviar_correo_asistencia(self, id_alumno, fecha, hora, correo, id, nombre_asignatura):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_user = 'registappnoreply@gmail.com'
        smtp_password = 'mwwi tgie xffz bhuv'
        hora_datetime = datetime.strptime(hora, "%H:%M:%S")
        hora_formateada = hora_datetime.strftime("%H:%M:%S")
        usuario = Usuario.objects.get(id_usuario = id_alumno)
        usuario = usuario.pnombre_usuario + ' ' + usuario.apaterno_usuario
        # Configuración del correo electrónico
        subject = 'Registro de Asistencia'
        body = f'Se registró la asistencia para el alumno {usuario} de la seccion {id} del ramo {nombre_asignatura} el {fecha} a las {hora_formateada}.'

        # Configuración del remitente y destinatario
        from_email = 'registappnoreply@gmail.com'
        to_email = correo

        # Creación del mensaje
        message = MIMEMultipart()
        message['From'] = from_email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        # Inicialización del servidor SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)

            # Envío del mensaje
            server.sendmail(from_email, to_email, message.as_string())
    
    def post(self, request):
        try:
            data = JSONParser().parse(request)
            id = data['id']
            clases = Clase.objects.filter(id_usuario=id).order_by('id_clase')
            serializer = ClaseSerializer(clases, many=True)
            
            asig = []
            profe = []
            for clase in clases:
                profe_id = clase.id_profesor_id
                profesor = Usuario.objects.get(id_profesor = profe_id)
                asignatura_id = clase.id_asignatura_id
                asignatura = Asignatura.objects.get(id_asignatura=asignatura_id)
                asig.append(asignatura)
                profe.append(profesor)
            
            profesor_serializers = UserSerializer(profe, many=True)
            asignatura_serializers = AsignaturaSerializer(asig, many=True)

            combined_data = []
            for i in range(len(clases)):
                clase_data = {
                   **serializer.data[i],
                    **asignatura_serializers.data[i],
                    **profesor_serializers.data[i],
                }
                combined_data.append(clase_data)


            return JsonResponse(combined_data, safe=False)
        except Exception as e:
            print(f'Error en la vista: {repr(e)}')
            return HttpResponseServerError('Error interno del servidor', content_type='text/plain')