from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    tipo_usuario = models.ForeignKey('tipoUsuario', on_delete=models.CASCADE, db_column='idTipo', blank=True, null=True)

class tipoUsuario(models.Model):
    id_tipoUsuario = models.AutoField(primary_key=True, db_column='idTipo', verbose_name='Tipo de ID')
    tipo_usuario = models.CharField(max_length=20, blank=True, null=True, unique=False, default='DEFAULT VALUE')

    def __str__(self):
        return str(self.tipo_usuario)
