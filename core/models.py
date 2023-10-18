from django.db import models

# Create your models here.
class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True, verbose_name='Id del Usuario')
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre del Usuario')
    direccion_usuario = models.CharField(max_length=50, verbose_name='Direccion del Usuario')
    password_usuario = models.CharField(max_length=50, verbose_name='Contrasenna del Usuario')
    mail_usuario = models.EmailField(unique=True, blank=True, null=True, max_length=100, verbose_name='Mail del Usuario')
    tipo_usuario = models.ForeignKey('tipoUsuario', on_delete=models.CASCADE, db_column='idTipo', blank=True, null=True)
#    num_telefono = models.ForeignKey('Telefono',  on_delete=models.CASCADE, db_column='Telefono')
#    direccion = models.ForeignKey('Direccion', on_delete=models.CASCADE, db_column='Direccion')

    def __str__(self):
        return str(self.nombre_usuario)
    
class tipoUsuario(models.Model):
    id_tipoUsuario = models.AutoField(primary_key=True, db_column='idTipo', verbose_name='Tipo de ID')
    tipo_usuario = models.CharField(max_length=20, blank=True, null=True, unique=False, default='DEFAULT VALUE')

    def __str__(self):
        return str(self.tipo_usuario)

# class Telefono(models.Model):
#     num_telefono = models.IntegerField(primary_key=True, verbose_name='Teléfono')
#     tipo_telefono = models.CharField(max_length=20, blank=True, default='Sin teléfono')
#     def __str__(self):
#         return self.num_telefono

# class Direccion(models.Model):
#     direccion = models.CharField(primary_key=True,max_length=70, verbose_name='Dirección')
#     id_comuna = models.ForeignKey('Comuna', on_delete=models.CASCADE, db_column='Id comuna')

#     def __str__(self):
#         return self.direccion
    
# class Comuna(models.Model):
#     id_comuna = models.AutoField(primary_key=True, verbose_name='Id comuna')
#     nombre_comuna = models.CharField(max_length=40, blank=False, null=False)
#     id_region = models.ForeignKey('Region', on_delete=models.CASCADE, db_column='Id region')

#     def __str__(self):
#         return self.nombre_comuna

# class Region(models.Model):
#     id_region = models.AutoField(primary_key=True, verbose_name='Id región')
#     nombre_region = models.CharField(max_length=40, blank=False, null=False)

#     def __str__(self):
#         return self.nombre_region