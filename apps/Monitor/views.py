from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from apps.Monitor.scripts.configurar import *
from apps.Comunicacion.views import *
from apps.Comunicacion.scripts.buscarpuertos import *
from apps.Monitor.scripts.hide import validarHide
from apps.Monitor.scripts.usuario import *
from apps.Monitor.scripts.control import *
from apps.Monitor.scripts.salida import *
from apps.Monitor.scripts.entrada import *
from apps.Monitor.scripts.comunicaciones import *
from apps.Monitor.scripts.programa import *
from apps.Monitor.scripts.escribircontrol import *
from apps.Controlador.scripts.lecturamonitor import *

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
        sesion['nivel'] = ''
        sesion['tipocontrol'] = ''
        sesion['confcontrolador'] = True
        
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

        puertos = buscarPuertos()
        data = {
            'puertos': puertos
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        sesion['puerto'] = request.POST['opcPuerto']
        sesion['velocidad'] = request.POST['opcVelocidad']
        sesion['controlador'] = request.POST['opcControl']

        return HttpResponseRedirect(self.success_url)

#Vista de los controladores donde se ve el SV y PV, y asi mismo se puede entrar a la configuracion de ellos
class Monitor(TemplateView):
    template_name = 'Monitor.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get(self, request, *args, **kwargs):
        sesion = request.session
        port = str(sesion['puerto'])
        vel = int(sesion['velocidad'])

        if str(sesion['manual1']) == '':
            sesion['manual1'] = 'botonNormal'
        
        if str(sesion['alarma1']) == '':
            sesion['alarma1'] = 'botonNormal'

        if str(sesion['manual2']) == '':
            sesion['manual2'] = 'botonNormal'
        
        if str(sesion['alarma2']) == '':
            sesion['alarma2'] = 'botonNormal'

        if str(sesion['cascada']) == '':
            sesion['cascada'] = 'botonNormal'
        
        infoMonitor = lecturamonitor(port, vel, request)

        data = {
            'controlador1': 1,
            'controlador2': 2,
            'manual1': str(sesion['manual1']),
            'manual2': str(sesion['manual2']),
            'alarma1': str(sesion['alarma1']),
            'alarma2': str(sesion['alarma2']),
            'cascada': str(sesion['cascada']),
            'lectura': str(sesion['salvando']),
            'pv1': infoMonitor[0],
            'sv1': infoMonitor[1],
            'out1': infoMonitor[2],
            'pv2': infoMonitor[3],
            'sv2': infoMonitor[4],
            'out2': infoMonitor[5],
        } 
        
        return render(request, self.template_name,data)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        port = str(sesion['puerto'])
        vel = int(sesion['velocidad'])
        data = {
            'controlador1': 1,
            'controlador2': 2,
            'manual1': str(sesion['manual1']),
            'manual2': str(sesion['manual2']),
            'alarma1': str(sesion['alarma1']),
            'alarma2': str(sesion['alarma2']),
            'cascada': str(sesion['cascada']),
            'lectura': str(sesion['salvando'])
        }
        
        if request.headers.get('x-requested-with') == 'XMLHttpRequest' and sesion.get('confcontrolador') :
            print(sesion.get('confcontrolador'))
            infoMonitor = lecturamonitor(port, vel, request)                        
            data['pv1'] = infoMonitor[0]
            data['sv1'] = infoMonitor[1]
            data['out1'] = infoMonitor[2]
            data['pv2'] = infoMonitor[3]
            data['sv2'] = infoMonitor[4]
            data['out2'] = infoMonitor[5]
            
            data = json.dumps(data)
           
            return HttpResponse(data, 'application/json')

        else:
            sesion['confcontrolador'] = False
            if 'configcon1' in request.POST:
                sesion['configcon'] = 1
            elif 'configcon2' in request.POST:
                sesion['configcon'] = 2

            data['pv1'] = sesion['pv1']
            data['sv1'] = sesion['sv1']
            data['out1'] = sesion['out1']
            data['pv2'] = sesion['pv2']
            data['sv2'] = sesion['sv2']
            data['out2'] = sesion['out2']

            return render(request, self.template_name, data)

#Vista del nivel del controlador de usuarios para configurar los parametros de este nivel
class Usuario(TemplateView):
    template_name = 'Usuario.html'
    success_url = reverse_lazy('usuario')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        sesion = request.session
        
        data = {
            'controlador': sesion['configcon'],
            'textDescription' : 'Descripción: Punto de consigna. \nRango: 4 ~ 20',
            'valor': 20
        }

        return render(request, self.template_name, data)


    def post(self, request, *args, **kwargs):
        sesion = request.session
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dir1 = int(request.POST['opcion'])
            valor = validarUsuario(request, dir1)
            
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2]
            }
            data = json.dumps(lista)
            
            return HttpResponse(data, 'application/json')

        else:    
            direccion = int(request.POST['parametro'])
            valor = float(request.POST['valor'])
            print(type(valor), valor)
            escribirControl(request, direccion, valor)
            data = {
                'controlador': sesion['configcon'],
                'valor' : valor,
                'textDescription' : request.POST['textDescription']             
            }
                    
            return render(request,self.template_name,data)    
            
#Vista del nivel del controlador de control para configurar los parametros de este nivel
class Control(TemplateView):
    template_name = 'Control.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        sesion = request.session
        data = {
            'controlador': sesion['configcon']
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dir1 = int(request.POST['opcion'])
            valor = validarControl(request, dir1)
            lista = {
                'valor': valor[0]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        else:
            valor = int(request.POST['valor'])
            direccion = int(request.POST['parametro'])
            escribirControl(request, direccion, valor)
            data = {
            'controlador': sesion['configcon']
            }
            return render(request, self.template_name, data)

#Vista del nivel del controlador de salida para configurar los parametros de este nivel
class Salida(TemplateView):
    template_name = 'Salida.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        sesion = request.session
        data = {
            'controlador': sesion['configcon']
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dir1 = int(request.POST['opcion'])
            valor = validarSalida(request, dir1)
            lista = {
                'valor': valor[0]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        else:
            valor = int(request.POST['valor'])
            direccion = int(request.POST['parametro'])
            escribirControl(request, direccion, valor)
            data = {
            'controlador': sesion['configcon']
            }
            return render(request, self.template_name, data)

#Vista del nivel del controlador de entrada para configurar los parametros de este nivel
class Entrada(TemplateView):
    template_name = 'Entrada.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        sesion = request.session
        data = {
            'controlador': sesion['configcon']
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dir1 = int(request.POST['opcion'])
            valor = validarEntrada(request, dir1)
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2],
                'limlosp': valor[3],
                'limhisp': valor[4]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        else:
            valor = int(request.POST['valor'])
            direccion = int(request.POST['parametro'])
            escribirControl(request, direccion, valor)
            data = {
            'controlador': sesion['configcon']
            }
            return render(request, self.template_name, data)

#Vista del nivel del controlador de comunicacion para configurar los parametros de este nivel
class Comunicacion(TemplateView):
    template_name = 'Comunicaciones.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        sesion = request.session
        data = {
            'controlador': sesion['configcon']
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dir1 = int(request.POST['opcion'])
            valor = validarComunicacion(request, dir1)
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        else:
            valor = int(request.POST['valor'])
            direccion = int(request.POST['parametro'])
            escribirControl(request, direccion, valor)
            data = {
            'controlador': sesion['configcon']
            }
            return render(request, self.template_name)

#Vista del nivel del controlador de programa para configurar los parametros de este nivel
class Programa(TemplateView):
    template_name = 'Programa.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        sesion = request.session
        data = {
            'controlador': sesion['configcon']
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dir1 = int(request.POST['opcion'])
            valor = validarPrograma(request, dir1)
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        else:
            valor = int(request.POST['valor'])
            direccion = int(request.POST['parametro'])
            escribirControl(request, direccion, valor)
            data = {
            'controlador': sesion['configcon']
            }
            return render(request, self.template_name, data)

#Vista del nivel del controlador de hide para configurar los parametros de este nivel
class Hide(TemplateView):
    template_name = 'Hide.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        sesion = request.session
        data = {
            'controlador': sesion['configcon']
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        print(request.POST)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            dir1 = int(request.POST['opcion'])
            valor = validarHide(request, dir1)
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        else:
            valor = int(request.POST['valor'])
            direccion = int(request.POST['parametro'])
            escribirControl(request, direccion, valor)
            return render(request, self.template_name)