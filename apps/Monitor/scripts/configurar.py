from apps.Comunicacion.scripts.control import *
from apps.Comunicacion.scripts.controlencoder import *
from apps.Alarma.scripts.alarma import *
from apps.Controlador.scripts.registro import *
from apps.Controlador.scripts.registroenconder import *
import json


def configurar(request):
    sesion = request.session
    sesion['controlarLectura'] = 1

    if sesion['salvando'] != '':
        while int(sesion['hiloParado']) == 0:
            Control().stopallthreads(sesion)

        # administrarpuerto codigo para cerrar el puerto

        datof = Registro()
        alarma = Alarma()
        alarma.setAlarma(0, datof.getFechaHora(), 0, 'Fin', 'Desconectado', 0, 0)
        alarma.ingresarRegistro()

    # adminpuerto = AdministrarPuerto
    ctr = Control()
    dato = Registro()
    # controles = Controladores()
    # lc = LeerControlador()

    sesion['threadRead'] = 0
    sesion['threadWrite'] = 0
    sesion['threadEvents'] = 0
    # sesion['administrarPuerto'] = adminpuerto
    sesion['control'] = json.dumps(ctr, default=controlEncoder)
    sesion['registro'] = json.dumps(dato, default=registroEncoder)
    # sesion['controles'] = controles
    # sesion['leer'] = lc
    sesion['curvas'] = ''
    sesion['cont'] = ''
    sesion['decimales1'] = '-1'
    sesion['decimales2'] = '-1'
    sesion['puerto'] = ''
    sesion['velocidad'] = 0
    sesion['controlador'] = 0
    sesion['controlador1'] = 999
    sesion['salvando'] = ''
    sesion['controlConfigurar'] = '999'
    sesion['estadoAlta1'] = 'Inactiva'
    sesion['estadoMedia1'] = 'Inactiva'
    sesion['estadoBaja1'] = 'Inactiva'
    sesion['estadoAlta2'] = 'Inactiva'
    sesion['estadoMedia2'] = 'Inactiva'
    sesion['estadoBaja2'] = 'Inactiva'
    sesion['escribiendoControlador'] = '0'
    sesion['histeresis'] = '5'

    if sesion['alta1'] == '':
        sesion['alta1'] = '-2000'

    if sesion['alta2'] == '':
        sesion['alta2'] = '-2000'

    if sesion['media1'] == '':
        sesion['media1'] = '-2000'

    if sesion['media2'] == '':
        sesion['media2'] = '-2000'

    if sesion['baja1'] == '':
        sesion['baja1'] = '-2000'

    if sesion['baja2'] == '':
        sesion['baja2'] = '-2000'

    sesion['alarmaHabilitada'] = 'disabled'

    if sesion['cascada'] == '':
        sesion['cascada'] = 'botonBlack'

    if sesion['manual1'] == '':
        sesion['manual1'] = 'botonBlack'

    if sesion['manual2'] == '':
        sesion['manual2'] = 'botonBlack'

    if sesion['alarma1'] == '':
        sesion['alarma1'] = 'botonBlack'

    if sesion['alarma2'] == '':
        sesion['alarma2'] = 'botonBlack'

    if sesion['presion'] == '':
        sesion['presion'] = 'SI'