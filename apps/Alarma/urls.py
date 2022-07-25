from django.urls import path
from apps.Alarma.views import *


urlpatterns = [
    path('Evento/', Evento.as_view(), name='evento'),
]
