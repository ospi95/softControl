from django.urls import path
from apps.Archivo.views import *


urlpatterns = [
    path('Exportar/', Exportar.as_view(), name='exportar'),
    path('Grafica/', Grafica.as_view(), name='grafica'),
    path('GraficaRun/', Graficarun.as_view(), name='graficaRun'),
    path('GraficaConfirmacion/', GraficaConfirmacion.as_view(), name='graficaConfirmacion'),
    path('GraficaFiltro/', GraficaFiltro.as_view(), name='graficaFiltro'),
]
