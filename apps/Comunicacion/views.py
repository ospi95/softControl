from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from apps.Comunicacion.scripts.conectar import *
# Create your views here.

#Vista para mostrar que se esta ejecutando la conexion del controlador
class Conectando(TemplateView):
    template_name = 'Conectando.html'


    def get(self, request, *args, **kwargs):
        sesion = request.session
        conectar(request)
        data = {
            'controladores': str(sesion['numeroControles'])
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        if int(sesion['numeroControles']) != 0:
            success_url = reverse_lazy('conectado')
        else:
            success_url = reverse_lazy('Noconectado')

        return HttpResponseRedirect(success_url)

class Conectado(TemplateView):

    template_name = 'Conectado.html'
    success_url = reverse_lazy('monitor')

    def post(self, request, *args, **kwargs):

        return HttpResponseRedirect(self.success_url)


class NoConectado(TemplateView):

    template_name = 'Noconectado.html'
