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
        sesion['confcontrolador'] = True

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
        
        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (sesion.get('confcontrolador')) :
            
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
            print('POST')
            sesion['confcontrolador'] = False
            if 'configcon1' in request.POST:
                sesion['configcon'] = 1
            elif 'configcon2' in request.POST:
                sesion['configcon'] = 2

            data['pv1'] = sesion.get('pv1','')
            data['sv1'] = sesion.get('sv1','')
            data['out1'] = sesion.get('out1','')
            data['pv2'] = sesion.get('pv2','')
            data['sv2'] = sesion.get('sv2','')
            data['out2'] = sesion.get('out2','')

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
            'controlador': sesion.get('configcon', 1),
            'textDescription' : 'Descripción: Punto de consigna. \nRango: 4 ~ 20',
            'valor': ''
        }

        return render(request, self.template_name, data)


    def post(self, request, *args, **kwargs):
        sesion = request.session
        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'opciones'):
            
            dir1 = int(request.POST['opcion'])
            valor = validarUsuario(request, dir1)
            
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2]
            }
            data = json.dumps(lista)
            
            return HttpResponse(data, 'application/json')

        elif (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'salir'):
            
            sesion['confcontrolador'] = True
            data = {
                'respuesta': 'Correcto'
            }
            data = json.dumps(data)
            return HttpResponse(data, 'application/json')

        else:
               
            direccion = int(request.POST['parametro'])
            valor = float(request.POST['valor'])
            
            escribirControl(request, direccion, valor)
            data = {
                'controlador': sesion['configcon'],
                'valor': valor,
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
            'controlador': sesion.get('configcon', 1),
            'textDescription' : 'Descripción: Banda proporcional para la salida 1.\nRango: 0.0~3000',
            'valor': ''
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session
        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'opciones'):
            dir1 = int(request.POST['opcion'])
            valor = validarControl(request, dir1)
            lista = {
                'valor': valor[0]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        elif (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'salir'):
            
            sesion['confcontrolador'] = True
            data = {
                'respuesta': 'Correcto'
            }
            data = json.dumps(data)
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
            'controlador': sesion.get('configcon', 1),
            'textDescription' : 'Descripción: Tipo de alarma 1.\nRango: 0~13, ver tabla 1 del manual de usuario del controlador',
            'valor': ''
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session

        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'opciones'):
            dir1 = int(request.POST['opcion'])
            valor = validarSalida(request, dir1)
            lista = {
                'valor': valor[0]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        elif (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'salir'):
            
            sesion['confcontrolador'] = True
            data = {
                'respuesta': 'Correcto'
            }
            data = json.dumps(data)
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
            'controlador': sesion.get('configcon', 1),
            'textDescription' : 'Descripción: Selecciona el tipo de entrada 1.\nRango: ver manual, tabla 4 del manual de usuario del controlador.\nNota: Para enviar el dato al controlador escriba 0 si la entrada es termocupla tipo K en el rango 1 (K1), 1 si la entrada es termocupla tipo K en el rango 2 y así sucesivamente según el orden en que aparece en la tabla 4 del manual de usuario del controlador, donde el valor para Lin es 24.',
            'valor': ''
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session

        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'opciones'):
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

        elif (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'salir'):
            
            sesion['confcontrolador'] = True
            data = {
                'respuesta': 'Correcto'
            }
            data = json.dumps(data)
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
            'controlador': sesion.get('configcon', 1),
            'textDescription' : 'Descripción: Velocidad de comunicación\nRango: 2.4K / 4.8K / 9.6K / 19.2K / 38.4K\nNota: Para enviar el dato al controlador escriba 0 para 2.4K, 1 para 4.8K, 2 para 9.6K, 3 para 19.2K ó 4 para 38.4K',
            'valor': ''
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session

        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'opciones'):
            dir1 = int(request.POST['opcion'])
            valor = validarComunicacion(request, dir1)
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        elif (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'salir'):
            
            sesion['confcontrolador'] = True
            data = {
                'respuesta': 'Correcto'
            }
            data = json.dumps(data)
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
            'controlador': sesion.get('configcon', 1),
            'textDescription' : 'Descripción: Monitorea en que segmento va el programa.\nRango: 1~8.\nNota: Solo de lectura',
            'valor': ''
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session

        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'opciones'):
            dir1 = int(request.POST['opcion'])
            valor = validarPrograma(request, dir1)
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        elif (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'salir'):
            
            sesion['confcontrolador'] = True
            data = {
                'respuesta': 'Correcto'
            }
            data = json.dumps(data)
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
            'controlador': sesion.get('configcon', 1),
            'textDescription' : 'Descripción: Muestra el parámetro con respecto a esta posición.\nRango: non~t2of.\nNota: no puede estar el mismo parámeto en diferentes posiciones, para cambiar el valor actual tenga en cuenta:\n0 = non; 1 = OutL; 2 = At; 3 = mAn; 4 = AL1S; 5 = AL1L; 6 = AL1U;\n7 = AL2S; 8 = AL2L; 9 = AL2U; 10 = AL3S; 11 = AL3L; 12 = AL3U;\n13 = SoAk; 14 = rAmp; 15 = PvoF; 16 = Pvrr; 17 = SvoF; 18 = Ct;\n19 = HbA; 20 = LbA; 21 = Lbd; 22 = SSY; 23 = SOut; 24 = StmE;\n25 = ruCY; 26 = t1SS; 27 = t1on; 28 = t1ES; 29 = t1oF; 30 = t2SS;\n31 = t2on; 32 = t2ES; 33 = t2oF;.',
            'valor': ''
        }

        return render(request, self.template_name, data)

    def post(self, request, *args, **kwargs):
        sesion = request.session

        if (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'opciones'):
            dir1 = int(request.POST['opcion'])
            valor = validarHide(request, dir1)
            lista = {
                'valor': valor[0],
                'losp': valor[1],
                'hisp': valor[2]
            }
            data = json.dumps(lista)
            return HttpResponse(data, 'application/json')

        elif (request.headers.get('x-requested-with') == 'XMLHttpRequest') and (request.POST['action'] == 'salir'):
            
            sesion['confcontrolador'] = True
            data = {
                'respuesta': 'Correcto'
            }
            data = json.dumps(data)
            return HttpResponse(data, 'application/json')

        else:
            valor = int(request.POST['valor'])
            direccion = int(request.POST['parametro'])
            escribirControl(request, direccion, valor)
            return render(request, self.template_name)