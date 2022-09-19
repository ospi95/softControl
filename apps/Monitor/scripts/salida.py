from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.leercontrolador import *

def validarSalida(request, dir1):
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
    losp = 0
    hisp = 0

    if salvando == 'En lectura...':
        ctr.read(puerto, vel, id1, id2, request)
    else:
        ctr.write(puerto, vel, id1, id2, request)

    if (dir1 == 50) or (dir1 == 54) or (dir1 == 58) or (dir1 == 68) or (dir1 == 70) or (dir1 == 72) or (dir1 == 74):
        residuo = valorActual % 60
        parteEntera = (valorActual - residuo) /60
        losp = 0
        hisp = 99.59
        decimales = 100
    elif (dir1 == 48) or (dir1 == 52) or (dir1 == 56):
        entero = True
        losp = 0
        hisp = 12
    elif (dir1 == 49) or (dir1 == 53) or (dir1 == 57):
        valorActual = valorActual/10
        decimales = 10
        losp = 0
        hisp = 200
    elif dir1 == 51:
        entero = True
        losp = 0
        hisp = 11
    elif (dir1 == 55) or (dir1 == 59):
        entero = True
        losp = 0
        hisp = 7
    elif dir1 == 60:
        entero = True
        losp = 0
        hisp = 1
    elif (dir1 == 62) or (dir1 == 63):
        valorActual = valorActual/10
        decimales = 10
        losp = 0
        hisp = 100
    elif (dir1 == 67) or (dir1 == 69) or (dir1 == 71) or (dir1 == 73):
        entero = True
        losp = 1
        hisp = 8

    if valorActual == 0:
        if dir1 == 60:
            valorActualString = 'CooL'
        elif dir1 == 64:
            valorActualString = 'Pv'
    elif valorActual == 1:
        if dir1 == 60:
            valorActualString = 'HEAt'
        elif dir1 == 64:
            valorActualString = 'Sv'
    elif (valorActual == 2) and (dir1 == 64):
        valorActualString = 'dEv'
    elif (valorActual == 2) and (dir1 == 64):
        valorActualString = 'Mv'
    else:
        if valorActual > 63535:
            valorActual = valorActual - 35536
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)
        else :
            valorActualString = valorActual

    return [valorActualString, losp, hisp]