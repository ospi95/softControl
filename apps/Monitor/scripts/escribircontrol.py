from apps.Comunicacion.scripts.control import *
from apps.Controlador.scripts.escribircontrolador import *
import math

def escribirControl(request, direccion, valor):
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

    client = ModbusSerialClient(
        method="rtu",
        port=puerto,
        stopbits=1,
        bytesize=8,
        parity='N',
        baudrate=vel
    )

    result = client.read_holding_registers(address=83, count=1, unit=id1)
    d = int(math.pow(10, result[0]))
    valor = valor*d
    ec.escribir(puerto, vel, id, direccion, valor)

    if salvando == 'En Lectura...':
        ctr.read(puerto, vel, id1, id2, request)
    else:
        ctr.write(puerto, vel, id1, id2, request)

    sesion['escribiendoControlador'] = 0