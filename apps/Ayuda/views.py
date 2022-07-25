from django.views.generic import TemplateView
# Create your views here.


class AcercaDe(TemplateView):

    template_name = 'AcercaDe.html'


class ManualControlador(TemplateView):

    template_name = 'Manual_Contr.html'


class ManualUsuario(TemplateView):

    template_name = 'Manual_Usu.html'
