from django.db import models


# Create your models here.

class Clase(models.Model):
    id_clase = models.CharField(primary_key=True, max_length=15, db_column='idClase', verbose_name='id de clase')
    total_clase = models.IntegerField(null=True, blank=True)
    clase_asistida = models.IntegerField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    hora = models.TimeField(auto_now_add=True, null=True)
    id_usuario = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='idUser', blank=True, null=True)
    id_profesor = models.ForeignKey('Usuario', on_delete=models.CASCADE, db_column='idProfesor', related_name='idProfesor', blank=True, null=True)
    id_asignatura = models.ForeignKey('Asignatura', on_delete=models.CASCADE, db_column='idAsignatura', blank=True, null=True)

class Asignatura(models.Model):
    id_asignatura = models.AutoField(primary_key=True, db_column='idAsignatura', verbose_name='id de asignatura')
    nombre_asignatura = models.CharField(max_length=25, verbose_name='Nombre de Aignatura')

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, db_column='idUser', verbose_name='id del Usuario')
    id_profesor = models.IntegerField(unique=True, db_column='idProfesor', null=True, blank=True, verbose_name='id del Profesor')
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre del Usuario')
    pnombre_usuario = models.CharField(max_length=25, verbose_name='Primer Nombre')
    apaterno_usuario = models.CharField(max_length=25, verbose_name='Apellido Usuario')
    direccion_usuario = models.CharField(max_length=50, verbose_name='Direccion del Usuario')
    password_usuario = models.CharField(max_length=50, verbose_name='Contrasenna del Usuario')
    mail_usuario = models.EmailField(unique=True, blank=True, null=True, max_length=100, verbose_name='Mail del Usuario')
    tipo_usuario = models.ForeignKey('tipoUsuario', on_delete=models.CASCADE, db_column='idTipo', blank=True, null=True)


class tipoUsuario(models.Model):
    id_tipoUsuario = models.AutoField(primary_key=True, db_column='idTipo', verbose_name='Tipo de ID')
    tipo_usuario = models.CharField(max_length=20, blank=True, null=True, unique=False, default='DEFAULT VALUE')

    def __str__(self):
        return str(self.tipo_usuario)
