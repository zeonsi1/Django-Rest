from django.contrib import admin
from core.models import Usuario,Clase,tipoUsuario

# Register your models here.

admin.site.register(Clase)
admin.site.register(Usuario)
admin.site.register(tipoUsuario)