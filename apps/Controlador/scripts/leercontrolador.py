import math
from ..scripts.registro import *
from apps.Controlador.scripts.controladores import *
from pymodbus.client.sync import ModbusSerialClient
from apps.Controlador.scripts.controladoresencoder import *
import json

class Leercontrolador:
    dato = Registro()
    controladores = Controladores()
    secuencia = 0
    fecha = datetime.now
    PV1 = 0
    SV1 = 0
    OUT1 = 0
    P1 = 0
    I1 = 0
    D1 = 0
    PV2 = 0
    SV2 = 0
    OUT2 = 0
    P2 = 0
    I2 = 0
    D2 = 0
    dir = 0
    d = 0

    def leer(self, port, vel, id1, id2):
        client = ModbusSerialClient(
            method="rtu",
            port=port,
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=vel
        )

        #LECTURA CONTROLADOR 1
        #Lectura del controlador (Numero decimales para PV y SV)
        result = client.read_holding_registers(address=83, count=1, unit=id1)
        d = int(math.pow(10, result.registers[0]))

        #Lectura del controlador (SV, OUT)
        result = client.read_holding_registers(address=2, count=2, unit=id1)
        sv1 = result.registers[0]
        out1 = result.registers[1]
        if sv1 > 63000:
            sv1 = sv1 - 65536
        sv1 = sv1/d
        out1 = out1/10

        #Lectura del controlador (Banda proporcional (P), tiempo integral (I) y tiempo derivativo (D))
        result = client.read_holding_registers(address=25, count=3, unit=id1)
        p1 = result.registers[0]
        p1 = p1/10
        i1 = result.registers[1]
        d1 = result.registers[2]

        #Lectura del controlador (PV)
        result = client.read_holding_registers(address=256, count=1, unit=id1)
        pv1 = result.registers[0]
        if pv1 > 63000:
            pv1 = pv1 - 65536
        pv1 = pv1/d


        # LECTURA CONTROLADOR 2
        if id2 != 999:
            # Lectura del controlador (Numero decimales para PV y SV)
            result = client.read_holding_registers(address=83, count=1, unit=id2)
            d = int(math.pow(10, result.registers[0]))

            # Lectura del controlador (SV, OUT)
            result = client.read_holding_registers(address=2, count=2, unit=id2)
            sv2 = result.registers[0]
            out2 = result.registers[1]
            if sv2 > 63000:
                sv2 = sv2 - 65536
            sv2 = sv1/d
            out2 = out2/10

            # Lectura del controlador (Banda proporcional (P), tiempo integral (I) y tiempo derivativo (D))
            result = client.read_holding_registers(address=25, count=3, unit=id2)
            p2 = result.registers[0]
            p2 = p2 / 10
            i2 = result[1]
            d2 = result[2]

            # Lectura del controlador (PV)
            result = client.read_holding_registers(address=256, count=1, unit=id2)
            pv2 = result.registers[0]
            if pv2 > 63000:
                pv2 = pv2 - 65536
            pv2 = pv2 / d

        self.dato.setRegistro(0,self.fecha, pv1, sv1, out1, p1, i1, d1, pv2, sv2, out2, p2, i2, d2)

        return self.dato

    def leerDireccion(self, port, vel, id1, dir1):
        client = ModbusSerialClient(
            method="rtu",
            port=port,
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=vel
        )

        result = client.read_holding_registers(address=dir1, count=1, unit=id1)
        d = 0
        k = 0
        while k < 3:
            try:
                k = k + 1
                d = result.registers[0]
                if d > 63000:
                    d = d - 65536
            finally:
                pass

            if client.connect():
                k = 3

        return d

    def leerControladores(self, port, vel, id1, id2, request):

        sesion = request.session
        self.controladores.setRegistro(999, 999)
        client = ModbusSerialClient(
            method="rtu",
            port=port,
            stopbits=1,
            bytesize=8,
            parity='N',
            baudrate=vel
        )

        # LECTURA CONTROLADOR 1
        result = client.read_holding_registers(address=90, count=1, unit=id1)
        self.controladores.setControlador1(result.registers[0])

        # LECTURA CONTROLADOR 2
        result = client.read_holding_registers(address=90, count=1, unit=id2)
        self.controladores.setControlador2(result.registers[0])

        sesion['controlares'] = json.dumps(self.controladores, default=controladoresEncoder)

        sesion['lecturaControles'] = 0