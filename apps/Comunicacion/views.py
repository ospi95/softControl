from django.views.generic import TemplateView
# Create your views here.


class Conectando(TemplateView):

    template_name = 'Conectando.html'


class Conectado(TemplateView):

    template_name = 'Conectado.html'


class NoConectado(TemplateView):

    template_name = 'Noconectado.html'
