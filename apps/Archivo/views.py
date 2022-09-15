from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import json
from random import randint
from django.urls import reverse_lazy
from apps.Archivo.scripts.checked import *
from apps.Archivo.scripts.rechecked import *

# Create your views here.


class Exportar(TemplateView):

    template_name = 'Exportar.html'


class Grafica(TemplateView):

    template_name = 'Grafica.html'
    success_url = reverse_lazy('home')
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        sesion = request.session
        
        data = {
            'cascada': str(sesion['cascada']),
            'lectura': '...En lectura' #str(sesion['salvando'])
        }

        return render(request, self.template_name, data)


    def post(self, request, *args, **kwargs):
        sesion = request.session

        data = checked(request)
        
        sesion['EstadoGrafica'] = data

        return render(request, self.template_name, data)


class Graficarun(TemplateView):
    template_name = 'Graficarun.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        sesion = request.session

        data = rechecked(request)

        return render(request, self.template_name, data)


    def post(self, request, *args, **kwargs):

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            lista = {
                'yPV1': randint(0,10),
                'ySV1': randint(0,15),
                'yOUT1': randint(0,20),
                'yP1': randint(0,30),
                'yI1': randint(0,40),
                'yD1': randint(0,50),
                'yPV2': randint(0,10),
                'ySV2': randint(0,15),
                'yOUT2': randint(0,20),
                'yP2': randint(0,30),
                'yI2': randint(0,40),
                'yD2': randint(0,50)
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')


class GraficaConfirmacion(TemplateView):
    template_name = 'GraficaConfirmacion.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        sesion = request.session

        data = rechecked(request)

        return render(request, self.template_name, data)