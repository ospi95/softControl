from apps.Comunicacion.scripts.control import *
from apps.Alarma.scripts.alarma import *
from apps.Comunicacion.scripts.administrarpuerto import *
from apps.Controlador.scripts.leercontrolador import *


def conectar(request):
    sesion = request.session
    ctr = Control()
    alarma = Alarma()
    adminpuertos = AdministrarPuerto()
    leercontrol = Leercontrolador()
    print("VALIDANDO.")

    controlador = sesion['controlador']
    puerto = str(sesion['puerto'])
    vel = int(sesion['velocidad'])
    adminpuertos.abrirPuerto(puerto, vel, request)
    numeroControles = 0
    sesion['controlador1'] = 999
    sesion['controlador2'] = 999
    id1 = 999
    id2 = 999

    if int(sesion['controlarLecturaPuerto']) == 1:
        sesion['controlarLecturaPuerto'] = 0
        #leercontrol.leerControladores(puerto, vel, 1, 2, request)
        client = ModbusSerialClient(
            method="rtu",
            port="COM3",
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=9600
        )        
        # LECTURA CONTROLADOR 1
        # result = client.read_holding_registers(address=90, count=1, unit=1)
        # sesion['controlador1'] = result.registers[0]
       
        # # LECTURA CONTROLADOR 2
        # result = client.read_holding_registers(address=90, count=1, unit=2)
        # sesion['controlador2'] = result.registers[0]
        print("CONECTADO",client.connect())
        if controlador == 'C1' or controlador == 'C3':
            if int(sesion['controlador1']) == 1:
                sesion['controlador1'] = 1
                id1 = 1
                numeroControles = numeroControles + 1
        if controlador == 'C2' or controlador == 'C3':
            if int(sesion['controlador2']) == 2:
                sesion['controlador2'] = 2
                id1 = 2
                numeroControles = numeroControles + 1

        sesion['controlador'] = numeroControles

        if numeroControles != 0:

            ctr.read(puerto, vel, id1, id2, request)

            sesion['salvando'] = 'En lectura...'
            fechaHora = datetime.now().isoformat()
            alarma.setAlarma(0, fechaHora, numeroControles, 'Inicio', 'Conectado', 0, 0)
            alarma.ingresarRegistro()

    sesion['numeroControles'] = numeroControles

    return()

