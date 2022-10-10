import json
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
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

        if int(sesion['numeroControles']) > 0:
            estadoenviar = 'enabled'
        else:
            estadoenviar = 'disabled' 
        
        if sesion['cascada'] == 'botonOrange':
            selectedCascada = 'selected'
        else:
            if sesion['nivel'] == 'NO':
                selectedFlujo = 'selected'
            else:
                selectedNivel = 'selected'

        data = {
            'estadoenviar': estadoenviar,
            'controladores': int(sesion['numeroControles']),
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
        print(request.POST)

        if int(sesion['numeroControles']) > 0:
            estadoenviar = 'enabled'
        else:
            estadoenviar = 'disabled' 

        if request.POST['tipocontrol'] == 'cascada':
            sesion['cascada'] = 'botonOrange'
        else:
            sesion['cascada'] = ''
        
        if request.POST['tipocontrol'] == 'cascada':
            selectedCascada = 'selected'
            sesion['tipocontrol'] = 'cascada'
        elif request.POST['tipocontrol'] == 'nivel':
            selectedNivel = 'selected'
            sesion['tipocontrol'] = 'nivel'
        elif request.POST['tipocontrol'] == 'flujo':
            selectedFlujo = 'selected'
            sesion['tipocontrol'] = 'flujo'

        data = {
            'estadoenviar': estadoenviar,
            'controladores': int(sesion['numeroControles']),
            'selectedCascada': selectedCascada,
            'selectedFlujo': selectedFlujo,
            'selectedNivel': selectedNivel
        }

        return render(request, self.template_name, data)

class Proceso(TemplateView):

    template_name = 'Proceso.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        sesion = request.session

        if sesion['tipocontrol'] == 'cascada':
            out = sesion.get('out2', '')
        elif sesion['tipocontrol'] == 'flujo':
            out = sesion.get('out2', '')
        else:
            out = sesion.get('out1', '')

        data = {
            'pv1': sesion.get('pv1', ''),
            'sv1': sesion.get('sv1', ''),
            'pv2': sesion.get('pv2', ''),
            'sv2': sesion.get('sv2', ''),
            'out': out,
            'cascada': str(sesion['cascada']),
            'lectura': str(sesion.get('salvando', '...Sin lectura'))
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if sesion['tipocontrol'] == 'cascada':
                out = sesion.get('out2', '')
            elif sesion['tipocontrol'] == 'flujo':
                out = sesion.get('out2', '')
            else:
                out = sesion.get('out1', '')

            lista = {
                'pv1': sesion.get('pv1', ''),
                'sv1': sesion.get('sv1', ''),
                'pv2': sesion.get('pv2', ''),
                'sv2': sesion.get('sv2', ''),
                'out': out,
                'cascada': str(sesion['cascada']),
                'lectura': str(sesion.get('salvando', '...Sin lectura'))
            }
            
            data = json.dumps(lista)
           
            return HttpResponse(data, 'application/json')

        else:
            return render(request, self.template_name, data)