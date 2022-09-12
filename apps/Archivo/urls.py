from django.urls import path
from apps.Archivo.views import *


urlpatterns = [
    path('Exportar/', Exportar.as_view(), name='exportar'),
    path('Grafica/', Grafica.as_view(), name='grafica')
]
