from django.urls import path
from rest_asistencia.views import lista_usuarios

urlpatterns = [
    path('lista_usuarios', lista_usuarios, name="lista_usuarios"),
]