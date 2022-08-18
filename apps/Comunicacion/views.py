from django.views.generic import TemplateView
from django.shortcuts import render
# Create your views here.

#Vista para mostrar que se esta ejecutando la conexion del controlador
class Conectando(TemplateView):
    template_name = 'Conectando.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)


class Conectado(TemplateView):

    template_name = 'Conectado.html'


class NoConectado(TemplateView):

    template_name = 'Noconectado.html'
