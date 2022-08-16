from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import TemplateView
from apps.Monitor.scripts.configurar import configurar
from apps.Alarma.scripts.alarmaencoder import *
from apps.Comunicacion.scripts.control import *
import json

import jsonpickle
# Create your views here.

class Home(TemplateView):
    template_name='Home.html'

    def get(self, request, *args, **kwargs):
        sesion = request.session

        sesion['sesion'] = 0
        sesion['salvando'] = ''
        sesion['LeeDireccion'] = 1
        sesion['hiloParado'] = 1
        sesion['alta1'] = ''
        sesion['alta2'] = ''
        sesion['media1'] = ''
        sesion['media2'] = ''
        sesion['baja1'] = ''
        sesion['baja2'] = ''
        sesion['cascada'] = ''
        sesion['manual1'] = ''
        sesion['manual2'] = ''
        sesion['alarma1'] = ''
        sesion['alarma2'] = ''
        sesion['presion'] = ''

        return render(request, self.template_name)


class Principal(TemplateView):
    template_name='Softcontrol.html'

    def get(self, request, *args, **kwargs):
        sesion = request.session

        if sesion['sesion'] == 0:
            configurar(request)
            sesion['sesion'] = 1

        return render(request, self.template_name)

    def post(self, request):
        pass


class Monitor(TemplateView):
    template_name = 'Monitor.html'