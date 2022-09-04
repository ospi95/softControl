from django.contrib import admin
from django.urls import include, path
from apps.Monitor.views import *


urlpatterns = [
    path('', Principal.as_view(), name='principal'),
    path('Monitor/', Monitor.as_view(), name='monitor'),
    path('Usuario/', Usuario.as_view(), name='usuario'),
    path('Control/', Control.as_view(), name='control'),
    path('Salida/', Salida.as_view(), name='salida'),
    path('Entrada/', Entrada.as_view(), name='entrada'),
    path('Comunicacion/', Comunicacion.as_view(), name='comunicacion'),
    path('Programa/', Programa.as_view(), name='programa'),
    path('Hide/', Hide.as_view(), name='hide')
]
