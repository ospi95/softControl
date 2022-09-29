from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.leercontrolador import *
import math

def validarHide(request, dir1):
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

    losp = 0
    hisp = 33

    if valorActual == 0:
        valorActualString = 'non'
    elif valorActual == 1:
        valorActualString = 'OutL'
    elif valorActual == 2:
        valorActualString = 'At'
    elif valorActual == 3:
        valorActualString = 'mAn'
    elif valorActual == 4:
        valorActualString = 'AL1S'
    elif valorActual == 5:
        valorActualString = 'AL1L'
    elif valorActual == 6:
        valorActualString = 'AL1U'
    elif valorActual == 7:
        valorActualString = 'AL2S'
    elif valorActual == 8:
        valorActualString = 'AL2L'
    elif valorActual == 9:
        valorActualString = 'AL2U'
    elif valorActual == 10:
        valorActualString = 'AL3S'
    elif valorActual == 11:
        valorActualString = 'AL3L'
    elif valorActual == 12:
        valorActualString = 'AL3U'
    elif valorActual == 13:
        valorActualString = 'SoAk'
    elif valorActual == 14:
        valorActualString = 'rAmp'
    elif valorActual == 15:
        valorActualString = 'PvoF'
    elif valorActual == 16:
        valorActualString = 'Pvrr'
    elif valorActual == 17:
        valorActualString = 'SvoF'
    elif valorActual == 18:
        valorActualString = 'Ct'
    elif valorActual == 19:
        valorActualString = 'HbA'
    elif valorActual == 20:
        valorActualString = 'LbA'
    elif valorActual == 21:
        valorActualString = 'Lbd'
    elif valorActual == 22:
        valorActualString = 'SSY'
    elif valorActual == 23:
        valorActualString = 'SOut'
    elif valorActual == 24:
        valorActualString = 'StmE'
    elif valorActual == 25:
        valorActualString = 'ruCY'
    elif valorActual == 26:
        valorActualString = 't1SS'
    elif valorActual == 27:
        valorActualString = 't1on'
    elif valorActual == 28:
        valorActualString = 't1ES'
    elif valorActual == 29:
        valorActualString = 't1oF'
    elif valorActual == 30:
        valorActualString = 't2SS'
    elif valorActual == 31:
        valorActualString = 't2on'
    elif valorActual == 32:
        valorActualString = 't2ES'
    elif valorActual == 33:
        valorActualString = 't2oF'
    elif valorActual > 63535:
        valorActual = valorActual - 35536
        if entero:
            valorActualString = str(int(valorActual))
        else:
            valorActualString = str(valorActual)
    else :
        valorActualString = valorActual 
    
    
    return [valorActualString, losp, hisp]