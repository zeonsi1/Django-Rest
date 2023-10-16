from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name='Id del Usuario')
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre del Usuario')
    direccion_usuario = models.CharField(max_length=50, verbose_name='Direccion del Usuario')
    password_usuario = models.CharField(max_length=50, verbose_name='Contrasenna del Usuario')
    def __str__(self):
        return self.nombre_usuario