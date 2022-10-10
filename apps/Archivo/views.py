from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import json
from random import randint
from django.urls import reverse_lazy
from apps.Archivo.scripts.checked import *
from apps.Archivo.scripts.filtrografica import filtrografica
from apps.Archivo.scripts.rechecked import *
from apps.Controlador.scripts.lecturagrafica import *
from apps.Alarma.models import Alarmas
import time

# Create your views here.

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
            'lectura': str(sesion['salvando'])
        }

        return render(request, self.template_name, data)


    def post(self, request, *args, **kwargs):
        sesion = request.session

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            
            datos = Registros.objects.all()
            datos.delete()

            lista = {
                'opcion': 'Confirmado de borrado'
            }

            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        else:
            data = checked(request)
    
            sesion['EstadoGrafica'] = data
            data['cascada'] = str(sesion['cascada'])
            data['lectura'] = str(sesion['salvando'])

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
        sesion = request.session
        port = str(sesion['puerto'])
        vel = int(sesion['velocidad'])

        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (sesion.get('confcontrolador')):
            graficando = lecturagrafica(port, vel)
            
            lista = {
                'yPV1': graficando[0],
                'ySV1': graficando[1],
                'yOUT1': graficando[2],
                'yP1': graficando[3],
                'yI1': graficando[4],
                'yD1': graficando[5],
                'yPV2': graficando[6],
                'ySV2': graficando[7],
                'yOUT2': graficando[8],
                'yP2': graficando[9],
                'yI2': graficando[10],
                'yD2': graficando[11]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')
        
        else:

            return render(request, self.template_name)

class GraficaConfirmacion(TemplateView):
    template_name = 'GraficaConfirmacion.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        sesion = request.session

        return render(request, self.template_name)

class GraficaFiltro(TemplateView):
    template_name = 'GraficaFiltro.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        sesion = request.session
        
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        sesion = request.session

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            
            start_date = request.POST['opcion[start_date]']
            end_date = request.POST['opcion[end_date]']

            lista = filtrografica(request, start_date, end_date)

            data = json.dumps(lista)

            return HttpResponse(data, 'application/json')
    
class GraficaConfirmacionFiltro(TemplateView):
    template_name = 'GraficaConfirmacionFiltro.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)