from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.escribircontrolador import *

def escribirControl(request, direccion):
    sesion = request.session
    sesion['escribiendoControlador'] = 1
    id = int(sesion['configcon'])
    vel = int(sesion['velocidad'])
    puerto = str(sesion['puerto'])
    ctr = Control()
    ec = Escribircontrolador()
    id1 = int(sesion['controlador1'])
    id2 = int(sesion['controlador2'])
    salvando = str(sesion['salvando'])

    ec.escribir(puerto, vel, id, direccion, request)

    if salvando == 'En Lectura...':
        ctr.read(puerto, vel, id1, id2, request)
    else:
        ctr.write(puerto, vel, id1, id2, request)

    sesion['escribiendoControlador'] = 0