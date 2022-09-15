from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.leercontrolador import *
import math

def validarControl(request, dir1):
    sesion = request.session
    puerto = str(sesion['puerto'])
    idx = int(sesion['configcon'])
    vel = int(sesion['velocidad'])
    id1 = int(sesion['controlador1'])
    id2 = int(sesion['controlador2'])
    entero = True
    ValorActual = -99999
    decimales = 1
    valorActualString = ''

    ctr = Control()
    leercontrol = Leercontrolador()
    salvando = sesion['salvando']

    valorActual = leercontrol.leerDireccion(puerto, vel, idx, dir1)
    losp = 0
    hisp = 0

    if salvando == 'En lectura...':
        ctr.read(puerto, vel, id1, id2, request)
    else:
        ctr.write(puerto, vel, id1, id2, request)

    if dir1 == 25:
        valorActual = valorActual / 10
        entero = False
        decimales = 10
        losp = 0
        hisp = 3000
    elif dir1 == 26:
        losp = 0
        hisp = 3600
    elif (dir1 == 27):
        losp = 0
        hisp = 900
    elif (dir1 == 28) or (dir1 == 29) or (dir1 == 38) (dir1 == 45):
        valorActual = valorActual / 10
        entero = False
        decimales = 10
        losp = 0
        hisp = 200
    elif (dir1 == 30) or (dir1 == 37):
        valorActual = valorActual / 10
        entero = False
        decimales = 10
        losp = -200
        hisp = 200
    elif (dir1 == 31) or (dir1 == 39):
        valorActual = valorActual / 10
        entero = False
        decimales = 10
        losp = 0
        hisp = 100
    elif dir1 == 40:
        losp = 0
        hisp = 10
    elif dir1 == 42:
        losp = 1
        hisp = 1000
    elif dir1 == 43:
        losp = 0
        hisp = 2
    elif (dir1 == 44) or (dir1 == 46) or (dir1 == 47):
        losp = 0
        hisp = 1

    if (valorActual == 0):
        if dir1 == 43:
            valorActualString = 'CoLd'
        elif dir1 == 47:
            valorActualString = 'Cont'
    elif (valorActual == 1):
        if dir1 == 43:
            valorActualString = 'rSET'
        elif dir1 == 44:
            valorActualString = 'RSEt'
        elif dir1 == 46:
            valorActualString = 'Pid'
        elif dir1 == 47:
            valorActualString = 'Stop'
    elif (valorActual == 2):
        if dir1 == 43:
            valorActualString = 'Hot'
        elif dir1 == 44:
            valorActualString = 'Pv'
        elif dir1 == 46:
            valorActualString = 'Lpid'
    else:
        if valorActual > 63535:
            valorActual = valorActual - 65536
        if entero:
            valorActualString = str(valorActual)

    return [valorActualString, losp, hisp]