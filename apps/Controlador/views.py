from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
# Create your views here.


class Tipocontrol(TemplateView):

    template_name = 'Tipocontrol.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        sesion = request.session
        selectedCascada = ''
        selectedFlujo = ''
        selectedNivel = ''

        """ if int(sesion['numeroControles']) > 0:
            estadoenviar = 'enabled'
        else:
            estadoenviar = 'disabled' """
        
        if sesion['cascada'] == 'botonOrange':
            selectedCascada = 'selected'
        else:
            if sesion['nivel'] == 'NO':
                selectedFlujo = 'selected'
            else:
                selectedNivel = 'selected'

        data = {
            'estadoenviar': 'enabled', #estadoenviar,
            'controladores': 2, #int(sesion['numeroControles']),
            'selectedCascada': selectedCascada,
            'selectedFlujo': selectedFlujo,
            'selectedNivel': selectedNivel
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        selectedCascada = ''
        selectedFlujo = ''
        selectedNivel = ''

        """ if int(sesion['numeroControles']) > 0:
            estadoenviar = 'enabled'
        else:
            estadoenviar = 'disabled' """

        if request.POST['control'] == 'cascada':
            sesion['cascada'] = 'botonOrange'
        else:
            sesion['cascada'] = ''
        
        if request.POST['control'] == 'cascada':
            selectedCascada = 'selected'
        elif request.POST['control'] == 'nivel':
            selectedNivel = 'selected'
        elif request.POST['control'] == 'flujo':
            selectedFlujo = 'selected'

        data = {
            'estadoenviar': 'enabled', #estadoenviar,
            'controladores': 2, #int(sesion['numeroControles']),
            'selectedCascada': selectedCascada,
            'selectedFlujo': selectedFlujo,
            'selectedNivel': selectedNivel
        }

        return render(request, self.template_name, data)

class Proceso(TemplateView):

    template_name = 'Proceso.html'