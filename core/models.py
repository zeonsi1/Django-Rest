from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    tipo_usuario = models.ForeignKey('tipoUsuario', on_delete=models.CASCADE, db_column='idTipo', blank=True, null=True)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, db_column='idUser', verbose_name='id del Usuario')
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
