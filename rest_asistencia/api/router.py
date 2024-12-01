from django.urls import path
from rest_asistencia.views import UserView, ClaseView, AsistenciaView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('asistencia/', ClaseView.as_view()),
    path('asistenciaA/', AsistenciaView.as_view()),
]
