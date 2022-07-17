"""softcontrol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from fractions import Fraction
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
      
    path('alarma/', include('apps.Alarma.urls'), name='alarma'),
    # path('archivo/', include('apps.Archivo.urls'), name='alarma'),
    # path('ayuda/', include('apps.Ayuda.urls'), name='alarma'),
    # path('comunicacion/', include('apps.Comunicacion.urls'), name='alarma'),
    # path('controlador/', include('apps.Controlador.urls'), name='alarma'),
    # path('monitor/', include('apps.Monitor.urls'), name='alarma'),
]
