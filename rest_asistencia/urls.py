from django.urls import path
from rest_asistencia.views import lista_usuarios, update_usuarios

urlpatterns = [
    path('lista_usuarios', lista_usuarios, name="lista_usuarios"),
    path('update_usuarios/<nombre_usuario>', update_usuarios, name="update_usuarios")
]