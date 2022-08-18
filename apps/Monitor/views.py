from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from apps.Monitor.scripts.configurar import *
from apps.Comunicacion.views import *


import jsonpickle
# Create your views here.

#Vista de inicio de pagina donde se inicializan algunas varibles en la sesion
class Home(TemplateView):
    template_name='Home.html'

    def get(self, request, *args, **kwargs):
        sesion = request.session

        sesion['controlarLecturaPuerto'] = 1
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

#Vista de pantalla principal donde se carga la configuración del sistema
class Principal(TemplateView):
    template_name='Softcontrol.html'
    success_url = reverse_lazy('conectando')

    def get(self, request, *args, **kwargs):
        sesion = request.session
        sesion['controlarLecturaPuerto'] = 1
        if sesion['sesion'] == 0:
            configurar(request)
            sesion['sesion'] = 1

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        sesion['puerto'] = request.POST['myBrowser']
        sesion['velocidad'] = request.POST['opcVelocidad']
        sesion['controlador'] = request.POST['opcControl']

        return HttpResponseRedirect(self.success_url)


class Monitor(TemplateView):
    template_name = 'Monitor.html'