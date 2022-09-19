from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.leercontrolador import *
import math

def validarComunicacion(request, dir1):
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
    decimales = int(math.pow(10, leercontrol.leerDireccion(puerto, vel, idx, 83)))

    losp = float(leercontrol.leerDireccion(puerto, vel, idx, 76))
    losp = losp / decimales
    hisp = float(leercontrol.leerDireccion(puerto, vel, idx, 77))
    hisp = hisp / decimales

    if dir1 == 90:
        losp = 0
        hisp = 31
    elif (dir1 >= 91) and (dir <= 93):
        if decimales != 1:
            valorActual = valorActual/decimales
            entero = False
    elif dir1 == 94:
        losp = 1
        hisp = 4
    elif (dir1 == 95) or (dir1 == 102) or (dir1 == 109) or (dir1 == 116):
        valorActual = valorActual/10
        entero = False
        decimales = 10
        losp = 0
        hisp = 3000
    elif (dir1 == 96) or (dir1 == 103) or (dir1 == 110) or (dir1 == 117):
        losp = 0
        hisp = 3600
    elif (dir1 == 97) or (dir1 == 104) or (dir1 == 111) or (dir1 == 118):
        losp = 0
        hisp = 900
    elif (dir1 == 98) or (dir1 == 105) or (dir1 == 112) or (dir1 == 119):
        valorActual = valorActual/10
        entero = False
        decimales = 10
        losp = 0
        hisp = 100
    
    if (valorActual == 0) and (dir1 == 89):
        losp = 0
        hisp = 4
        valorActualString = '2.4K'
    elif (valorActual == 1) and (dir1 == 89):
        losp = 0
        hisp = 4
        valorActualString = '4.8K'
    elif (valorActual == 2) and (dir1 == 89):
        losp = 0
        hisp = 4
        valorActualString = '9.6K'
    elif (valorActual == 3) and (dir1 == 89):
        losp = 0
        hisp = 4
        valorActualString = '19.2K'
    elif (valorActual == 4) and (dir1 == 89):
        losp = 0
        hisp = 4
        valorActualString = '38.4K'
    else:
        if valorActual > 63535:
            valorActual = valorActual - 35536
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)
        else:
            valorActualString = valorActual
    
    return [valorActualString, losp, hisp]