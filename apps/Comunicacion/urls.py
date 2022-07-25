from django.urls import path
from apps.Comunicacion.views import *


urlpatterns = [
    path('Conectando/', Conectando.as_view(), name='conectando'),
    path('Conectado/', Conectado.as_view(), name='conectado'),
    path('No_Conectado/', NoConectado.as_view(), name='Noconectado'),
]
