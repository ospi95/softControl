from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.leercontrolador import *
import math

def validarEntrada(request, dir1):
    sesion = request.session
    puerto = str(sesion['puerto'])
    idx = int(sesion['configcon'])
    vel = int(sesion['velocidad'])
    id1 = int(sesion['controlador1'])
    id2 = int(sesion['controlador2'])
    entero = True
    ValorActual = -99999
    limlosp = 0
    limhisp = 100
    decimales = 1
    valorActualString = ''

    ctr = Control()
    leercontrol = Leercontrolador()
    salvando = sesion['salvando']

    valorActual = leercontrol.leerDireccion(puerto, vel, idx, dir1)
    tipoIn = leercontrol.leerDireccion(puerto, vel, idx, 75)
    unit = leercontrol.leerControladores(puerto, vel, idx, 82)
    decimales = int(math.pow(10, leercontrol.leerDireccion(puerto, vel, idx, 83)))

    losp = float(leercontrol.leerDireccion(puerto, vel, idx, 76))
    losp = losp / decimales
    hisp = float(leercontrol.leerDireccion(puerto, vel, idx, 77))
    hisp = hisp / decimales

    if decimales != 1:
        entero = False

    if dir1 == 75:
        losp = 0
        hisp = 24
    elif (dir1 == 78) or (dir1 == 79):
        losp = -1999
        hisp = 9999
    elif (dir1 == 80) or (dir1 == 81):
        losp = 0
        hisp = 65535
    elif dir1 == 82:
        losp = 0
        hisp = 2
    elif dir1 == 83:
        losp = 0
        hisp = 3
    elif dir1 == 84:
        losp = 0
        hisp = 1
        valorActual = valorActual/1000
        entero = False
        decimales = 1000

    if (valorActual == 0) and (dir1 == 75):
        valorActualString = 'K1'
    elif (valorActual == 1) and (dir1 == 75):
        valorActualString = 'K2'
    elif (valorActual == 2) and (dir1 == 75):
        valorActualString = 'K3'
    elif (valorActual == 3) and (dir1 == 75):
        valorActualString = 'K4'
    elif (valorActual == 4) and (dir1 == 75):
        valorActualString = 'K5'
    elif (valorActual == 5) and (dir1 == 75):
        valorActualString = 'j1'
    elif (valorActual == 6) and (dir1 == 75):
        valorActualString = 'j2'
    elif (valorActual == 7) and (dir1 == 75):
        valorActualString = 'j3'
    elif (valorActual == 8) and (dir1 == 75):
        valorActualString = 'j4'
    elif (valorActual == 9) and (dir1 == 75):
        valorActualString = 'j5'
    elif (valorActual == 10) and (dir1 == 75):
        valorActualString = 't1'
    elif (valorActual == 11) and (dir1 == 75):
        valorActualString = 't2'
    elif (valorActual == 12) and (dir1 == 75):
        valorActualString = 't3'
    elif (valorActual == 13) and (dir1 == 75):
        valorActualString = 'r'
    elif (valorActual == 14) and (dir1 == 75):
        valorActualString = 'E'
    elif (valorActual == 15) and (dir1 == 75):
        valorActualString = 'S'
    elif (valorActual == 16) and (dir1 == 75):
        valorActualString = 'b'
    elif (valorActual == 17) and (dir1 == 75):
        valorActualString = 'n'
    elif (valorActual == 18) and (dir1 == 75):
        valorActualString = 'Pt1'
    elif (valorActual == 19) and (dir1 == 75):
        valorActualString = 'Pt2'
    elif (valorActual == 20) and (dir1 == 75):
        valorActualString = 'Pt3'
    elif (valorActual == 21) and (dir1 == 75):
        valorActualString = 'Pt4'
    elif (valorActual == 22) and (dir1 == 75):
        valorActualString = 'Pt5'
    elif (valorActual == 23) and (dir1 == 75):
        valorActualString = 'jPt'
    elif (valorActual == 24) and (dir1 == 75):
        valorActualString = 'Lin'
    elif dir1 == 76:
        if (tipoIn == 0) or (tipoIn == 1) or (tipoIn == 2) or (tipoIn == 3) or (tipoIn == 4) or (tipoIn == 5) or (tipoIn == 6) or (tipoIn == 7) or (tipoIn == 8) or (tipoIn == 9) or (tipoIn == 13) or (tipoIn == 14) or (tipoIn == 15) or (tipoIn == 16) or (tipoIn == 19) or (tipoIn == 20) or (tipoIn == 21):
            valorActual = valorActual/decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limlosp = 0
            else:
                limlosp = 32
        elif (tipoIn == 10) or (tipoIn == 18):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limlosp = -50
            else:
                limlosp = -58
        elif (tipoIn == 11):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limlosp = -100
            else:
                limlosp = -148
        elif (tipoIn == 12) or (tipoIn == 17) or (tipoIn == 22) or (tipoIn == 23):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limlosp = -200
            else:
                limlosp = -328
        elif (tipoIn == 24):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)
            limlosp = -1999
    elif dir1 == 77:
        if (tipoIn == 0) or (tipoIn == 5) or (tipoIn == 20):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 200
            else:
                limhisp = 392
        elif (tipoIn == 1) or (tipoIn == 6) or (tipoIn == 12) or (tipoIn == 21):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 400
            else:
                limhisp = 752
        elif (tipoIn == 2) or (tipoIn == 7):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 800
            else:
                limhisp = 1472
        elif (tipoIn == 3) or (tipoIn == 8) or (tipoIn == 14):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 1000
            else:
                limhisp = 1832
        elif (tipoIn == 4) or (tipoIn == 9):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 1200
            else:
                limhisp = 2192
        elif (tipoIn == 10) or (tipoIn == 18):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 50
            else:
                limhisp = 122
        elif (tipoIn == 11) or (tipoIn == 19):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 100
            else:
                limhisp = 212
        elif (tipoIn == 13) or (tipoIn == 15):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 1700
            else:
                limhisp = 3092
        elif (tipoIn == 16):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 1800
            else:
                limhisp = 3272
        elif (tipoIn == 17):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 1300
            else:
                limhisp = 2372
        elif (tipoIn == 22):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 600
            else:
                limhisp = 1112
        elif (tipoIn == 23):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            if unit == 0:
                limhisp = 500
            else:
                limhisp = 932
        elif (tipoIn == 24):
            valorActual = valorActual / decimales
            if entero:
                valorActualString = str(int(valorActual))
            else:
                valorActualString = str(valorActual)

            limhisp = 9999

        elif valorActual == 0:
            if dir1 == 80:
                valorActualString = str(int(valorActual))
            elif dir1 == 81:
                valorActualString = str(int(valorActual))
            elif dir1 == 82:
                valorActualString = 'ºC'
        elif (valorActual == 1) and (dir1 == 82):
            valorActualString = 'ºF'
        elif (valorActual == 2) and (dir1 == 82):
            valorActualString = 'non'
        else:
            if valorActual > 63535:
                valorActual = valorActual - 35536
                if entero:
                    valorActualString = str(int(valorActual))
                else:
                    valorActualString = str(valorActual)

    return [valorActualString, losp, hisp]