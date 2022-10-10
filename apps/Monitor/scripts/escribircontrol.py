from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.escribircontrolador import *
from apps.Controlador.scripts.leercontrolador import *
import math

def escribirControl(request, direccion, valor):
    sesion = request.session
    
    sesion['escribiendoControlador'] = 1
    id = int(sesion['configcon'])
    vel = int(sesion['velocidad'])
    puerto = str(sesion['puerto'])
    ctr = Control()
    leercontrol = Leercontrolador()
    ec = Escribircontrolador()
    id1 = int(sesion['controlador1'])
    id2 = int(sesion['controlador2'])
    salvando = str(sesion['salvando'])

    decimales = int(math.pow(10, leercontrol.leerDireccion(puerto, vel, id, 83)))
    al1f = int(leercontrol.leerDireccion(puerto, vel, id, 48))
    al2f = int(leercontrol.leerDireccion(puerto, vel, id, 52))
    al3f = int(leercontrol.leerDireccion(puerto, vel, id, 56))
    
    if (direccion == 16) or (direccion == 17) or (direccion == 19) or (direccion == 3) or (direccion == 6) or (direccion == 7) or (direccion == 8) :
        valor = valor * 10
    elif direccion == 18:
        valor = valor * 1000
    elif direccion == 24:
        valor = 0
    elif (direccion == 2) or (direccion == 256):
        valor = valor * decimales
    elif direccion == 15:
        residuo = valor % 60
        parteEntera = (valor-residuo)/60
        valor = parteEntera + (residuo/100)
        
    elif (direccion >= 9) and (direccion <= 11):
        if al2f == 0:
            valor = valor
        elif (al2f == 1) or (al2f == 2):
            if (direccion == 10) or (direccion == 11):
                valor = valor
            else:
                valor = valor * 10
        elif (al2f == 3) or (al2f == 4):
            if (direccion == 10) or (direccion == 11):
                valor = valor
            else:
                valor = valor/decimales
        elif (al2f == 5) or (al2f == 6):
            if direccion == 9:
                valor = valor
            else:
                valor = valor * 10
        elif (al2f == 7) or (al2f == 8) or (al2f == 9):
            valor = valor
        elif al2f == 10:
            if (direccion == 10) or (direccion == 11):
                valor = valor
            else:
                valor = valor
        elif (al2f == 11) or (al2f == 12) or (al2f == 13):
            valor = valor
    elif (direccion >= 12) and (direccion <= 14):
        if al3f == 0:
            valor = valor
        elif (al3f == 1) or (al3f == 2):
            if (direccion >= 13) or (direccion <= 14):
                valor = valor
            else:
                valor = valor * 10
        elif (al3f == 3) or (al3f == 4):
            if (direccion >= 13) or (direccion <= 14):
                valor = valor
            else:
                valor = valor/decimales
        elif (al3f == 5) or (al3f == 6):
            if (direccion >= 13) or (direccion <= 14):
                valor = valor
            else:
                valor = valor * 10
        elif (al3f == 7) or (al3f == 8) or (al3f == 9):
            valor = valor
        elif al3f == 10:
            if (direccion == 13) or (direccion == 14):
                valor = valor
            else:
                valor = valor
        elif (al3f == 11) or (al3f == 12) or (al3f == 13):
            valor = valor
    elif direccion == 25:
        valor = valor * 10
    elif direccion == 26:
        valor = valor
    elif (direccion == 27):
        valor = valor
    elif (direccion == 28) or (direccion == 29) or (direccion == 38) (direccion == 45):
        valor = valor * 10
    elif (direccion == 30) or (direccion == 37):
        valor = valor * 10
    elif (direccion == 31) or (direccion == 39):
        valor = valor * 10
    elif direccion == 40:
        valor = valor
    elif direccion == 42:
        valor = valor
    elif direccion == 43:
        valor = valor
    elif (direccion == 44) or (direccion == 46) or (direccion == 47):
        valor = valor

    ec.escribir(puerto, vel, id, direccion, int(valor))

    if salvando == 'En Lectura...':
        ctr.read(puerto, vel, id1, id2, request)
    else:
        ctr.write(puerto, vel, id1, id2, request)

    sesion['escribiendoControlador'] = 0