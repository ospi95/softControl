from django.urls import path
from apps.Controlador.views import *


urlpatterns = [
    path('TipoControl/', Tipocontrol.as_view(), name='tipocontrol'),
    path('Proceso/', Proceso.as_view(), name='proceso'),
]
