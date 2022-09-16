from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.leercontrolador import *
import math

def validarUsuario(request, dir1):
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
    print(valorActual)
    decimales = int(math.pow(10, leercontrol.leerDireccion(puerto, vel, idx, 83)))
    estado = ''

    losp = float(leercontrol.leerDireccion(puerto, vel, idx, 76))
    losp = losp/decimales
    hisp = float(leercontrol.leerDireccion(puerto, vel, idx, 77))
    hisp = hisp/decimales

    al1f = int(leercontrol.leerDireccion(puerto, vel, idx, 48))
    al2f = int(leercontrol.leerDireccion(puerto, vel, idx, 52))
    al3f = int(leercontrol.leerDireccion(puerto, vel, idx, 56))

    if salvando == 'En lectura...':
        ctr.read(puerto, vel, id1, id2, request)
    else:
        ctr.write(puerto, vel, id1, id2, request)

    if dir1 == 16:
        valorActual = valorActual / 10
        decimales = 10
        losp = 0
        hisp = 200
    elif dir1 == 18:
        valorActual = valorActual / 1000
        decimales = 1000
        losp = 0
        hisp = 1
    elif dir1 == 24:
        entero = True
        losp = 0
        hisp = 1000
    elif dir1 == 2:
        valorActual = valorActual / decimales
    elif dir1 == 17 or dir1 == 19:
        valorActual = valorActual / 10
        decimales = 10
        losp = -200
        hisp = 200
    elif dir1 == 3:
        valorActual = valorActual / 10
        decimales = 10
        losp = 0
        hisp = 100
    elif dir1 == 256:
        valorActual = valorActual / decimales
        estado = 'disabled'
    elif dir1 == 15:
        residuo = valorActual % 60
        parteEntera = (valorActual-residuo)/60
        valorActual = parteEntera + (residuo/100)
        losp = 0
        hisp = 99.59
        decimales = 100
    elif (dir1 >= 6) and (dir1 <= 8):
        if al1f == 0:
            valorActual = -99999
            entero = True
            estado = "disabled"
        elif al1f == 1:
            if (dir1 == 7) or (dir1 == 8):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/10
                decimales = 10
                losp = 0
                hisp = 200
        elif (al1f == 2) or (al1f == 3):
            if (dir1 == 7) or (dir1 == 8):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/10
                decimales = 10
                losp = 0
                hisp = 200
        elif al1f == 4:
            if (dir1 == 7) or (dir1 == 8):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/decimales
        elif (al1f == 5) or (al1f == 6):
            if (dir1 == 6):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/10
                decimales = 10
                losp = 0
                hisp = 200
        elif (al1f == 7) or (al1f == 8) or (al1f == 9) or (al1f == 11) or (al1f == 12) or (al1f == 13):
            valorActual = -99999
            entero = True
            estado = "disabled"
        elif al1f == 10:
            if (dir1 == 7) or (dir1 == 8):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                entero = True
                losp = 1
                hisp = 8
    elif (dir1 >= 9) and (dir1 <= 11):
        if al2f == 0:
            valorActual = -99999
            entero = True
            estado = "disabled"
        elif (al2f == 1) or (al2f == 2):
            if (dir1 == 10) or (dir1 == 11):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/10
                decimales = 10
                losp = 0
                hisp = 200
        elif (al2f == 3) or (al2f == 4):
            if (dir1 == 10) or (dir1 == 11):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/decimales
        elif (al2f == 5) or (al2f == 6):
            if dir1 == 9:
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/10
                decimales = 10
                losp = 0
                hisp = 200
        elif (al2f == 7) or (al2f == 8) or (al2f == 9):
            valorActual = -99999
            entero = True
            estado = "disabled"
        elif al2f == 10:
            if (dir1 == 10) or (dir1 == 11):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                entero = True
                losp = 1
                hisp = 8
        elif (al2f == 11) or (al2f == 12) or (al2f == 13):
            entero = True
            estado = "disabled"
    elif (dir1 >= 12) and (dir1 <= 14):
        if al3f == 0:
            valorActual = -99999
            entero = True
            estado = "disabled"
        elif (al3f == 1) or (al3f == 2):
            if (dir1 >= 13) or (dir1 <= 14):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/10
                decimales = 10
                losp = 0
                hisp = 200
        elif (al3f == 3) or (al3f == 4):
            if (dir1 >= 13) or (dir1 <= 14):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual/decimales
        elif (al3f == 5) or (al3f == 6):
            if (dir1 >= 13) or (dir1 <= 14):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                valorActual = valorActual / 10
                decimales = 10
                losp = 0
                hisp = 200
        elif (al3f == 7) or (al3f == 8) or (al3f == 9):
            valorActual = -99999
            entero = True
            estado = "disabled"
        elif al3f == 10:
            if (dir1 == 13) or (dir1 == 14):
                valorActual = -99999
                entero = True
                estado = "disabled"
            else:
                entero = True
                losp = 1
                hisp = 8
        elif (al3f == 11) or (al3f == 12) or (al3f == 13):
            valorActual = -99999
            entero = True
            estado = "disabled"

    if (valorActual == 0) and (dir1 == 4):
        entero = True
        valorActualString = "no"
        losp = 0
        hisp = 1
    elif (valorActual == 1) and (dir1 == 4):
        entero = True
        valorActualString = "yes"
        losp = 0
        hisp = 1
    elif (valorActual == 0) and (dir1 == 5):
        entero = True
        valorActualString = "no"
        losp = 0
        hisp = 2
    elif (valorActual == 1) and (dir1 == 5):
        entero = True
        valorActualString = "man1"
        losp = 0
        hisp = 2
    elif (valorActual == 2) and (dir1 == 5):
        entero = True
        valorActualString = "man2"
        losp = 0
        hisp = 2
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