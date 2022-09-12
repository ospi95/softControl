from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
import json
from random import randint
# Create your views here.


class Exportar(TemplateView):

    template_name = 'Exportar.html'


class Grafica(TemplateView):
    template_name = 'Grafica.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        
        data = {
            'valorPV1': 'activate',
            'valorSV1': '',
            'valorOUT1': '',
            'valorP1': 'activate',
            'valorI1': 'activate',
            'valorD1': 'activate'
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        print(request.POST)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            lista = {
                'yPV1': randint(0,10),
                'ySV1': randint(0,15),
                'yOUT1': randint(0,20),
                'yP1': randint(0,30),
                'yI1': randint(0,40),
                'yD1': randint(0,50)
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')