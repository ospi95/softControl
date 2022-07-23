from django.contrib import admin
from django.urls import include, path
from apps.Ayuda.views import *


urlpatterns = [
    path('Acercade/', AcercaDe.as_view(), name='acercade'),

]
