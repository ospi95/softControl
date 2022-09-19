from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.leercontrolador import *
import math

def validarPrograma(request, dir1):
    sesion = request.session
    puerto = str(sesion['puerto'])
    idx = int(sesion['configcon'])
    vel = int(sesion['velocidad'])
    id1 = int(sesion['controlador1'])
    id2 = int(sesion['controlador2'])
    entero = False
    ValorActual = -99999

    decimales = 1
    valorActualString = ''

    ctr = Control()
    leercontrol = Leercontrolador()
    salvando = sesion['salvando']

    valorActual = leercontrol.leerDireccion(puerto, vel, idx, dir1)
    decimales = int(math.pow(10, leercontrol.leerDireccion(puerto, vel, idx, 83)))

    losp = float(leercontrol.leerDireccion(puerto, vel, idx, 76))
    losp = losp/decimales
    hisp = float(leercontrol.leerDireccion(puerto, vel, idx, 77))
    hisp = hisp/decimales

    if (dir1 == 123) or (dir1 == 125):
        entero = True
        losp = 1
        hisp = 8
        decimales = 1
    elif (dir1 == 126) or (dir1 == 129) or (dir1 == 132) or (dir1 == 135) or (dir1 == 138) or (dir1 == 141) or (dir1 == 144) or (dir1 == 147):
        if decimales == 1:
            entero = True
        else:
            valorActual = valorActual/decimales
    else:
        residuo = valorActual % 60
        parteEntera = (valorActual-residuo)/60
        valorActual = parteEntera + (residuo/100)
        losp = 0
        hisp = 99.59
        decimales = 100
    
    if valorActual > 63535:
        valorActual = valorActual - 35536
        if entero:
            valorActualString = str(int(valorActual))
        else:
            valorActualString = str(valorActual)
    else :
        valorActualString = valorActual 