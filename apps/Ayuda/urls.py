from django.urls import path
from apps.Ayuda.views import *


urlpatterns = [
    path('Acercade/', AcercaDe.as_view(), name='acercade'),
    path('Manual_Controlador/', ManualControlador.as_view(), name='manualcontrolador'),
    path('Manual_Usuario/', ManualUsuario.as_view(), name='manualusuario'),
    path('PID/', Diagrama.as_view(), name='diagramaPID'),
]
